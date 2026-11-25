"""The proposal contract. See PHASE-2.md task 2.1.

Return a full block, not a diff — diffs fail to apply constantly and every
failure teaches nothing about what this phase is actually testing. Switch
to search-and-replace edits in Phase 3, not before.

Parse strictly with a sentinel; never carry code through JSON — escaping
code through JSON produces failures that look like model problems and
aren't.
"""

from __future__ import annotations

import os
import re

from openai import AsyncOpenAI, OpenAI

from harness.judge import judge_client  # reuses the same LiteLLM-backed client construction

BLOCK = re.compile(r"<candidate>\n(.*?)\n</candidate>", re.S)
# Fallback for a response that opens the tag but never closes it. Found
# live running capability_case's first real hill-climb, 2026-09-22: ~30-40%
# of proposals hit exactly this pattern for this solution (0% for fixture/
# itot_classifier's shorter code-body rewrites) — the response reliably
# finishes on a complete, coherent sentence, it just sometimes forgets the
# closing sentinel after a long, essay-length rewrite. Not truncation (no
# max_tokens is set on this call, and the endings don't look cut off
# mid-word) — a real proposal discarded over a formatting slip, not a
# malformed one. Only tried when the strict pattern above doesn't match.
BLOCK_UNCLOSED = re.compile(r"<candidate>\n(.*)", re.S)

SYSTEM_PROMPT = """You improve one component of a larger system. You will be given the current
version and how it scored. Return one improved version.

Rules:
- "Current version" below is the BODY of an existing function — statements
  only. It is not a whole file and not a whole function definition. Do not
  write a `def` line, a docstring for a new function, or top-level imports
  it doesn't already use. Your response replaces those exact statements,
  nothing else, and gets embedded verbatim back into the same surrounding
  function.
- Return the complete replacement body. Not a diff, not an explanation.
- Wrap it in <candidate> and </candidate>, each on its own line.
- The function signature this body lives inside is frozen and not shown to
  you — do not attempt to redefine it.
- Do not import from fitness, evaluator, or tasks.
- Anything outside the block is discarded."""

# For executes_code=False solutions (PHASE-1.md's in-process/text path) —
# the artifact is instructions text embedded into a larger prompt template,
# not a Python function body, so the code-shaped wording above ("statements
# only", "def line", "function signature") would actively mislead the
# model. First real use: solutions/capability_case, the first text-artifact
# solution onboarded.
TEXT_SYSTEM_PROMPT = """You improve one component of a larger system: a block of instructions given
to another model, which reads a scenario and produces a judgment. You will
be given the current instructions and how they scored. Return one improved
version.

Rules:
- "Current version" below is the instructions text itself, not a full
  prompt template — it gets embedded verbatim into a fixed surrounding
  template (the scenario, the output format) that is not shown to you and
  is not yours to change.
- Return the complete replacement instructions text. Not a diff, not an
  explanation, not commentary about the change.
- Wrap it in <candidate> and </candidate>, each on its own line.
- The output format the instructed model must follow is fixed elsewhere —
  do not redefine it, but you may improve how the instructions explain it.
- Anything outside the block is discarded."""

USER_TEMPLATE = """## What this component must do
{task_description}
{standing_lessons}
## Current version
This is the body of the function — not a full file, not a def line.
<candidate>
{parent_block}
</candidate>
{inspirations}
## How it scored
quality {quality:.3f}   cost {cost_tokens} tokens   latency {latency:.1f}s

## Where it lost points
{failed_checks}
{retrieved_lessons}
Return one improved version."""


def parse_candidate(text: str) -> str | None:
    m = BLOCK.search(text)
    if m:
        body = m.group(1)
        return body if body.strip() else None
    m = BLOCK_UNCLOSED.search(text)
    if not m:
        return None
    body = m.group(1).rstrip()
    if body.endswith("</candidate>"):
        body = body[: -len("</candidate>")].rstrip()
    return body if body.strip() else None


def _messages(
    task_description: str,
    parent_block: str,
    quality: float,
    cost_tokens: int,
    latency: float,
    failed_checks: str,
    system_prompt: str = SYSTEM_PROMPT,
    standing_lessons: str = "",
    retrieved_lessons: str = "",
    inspirations: str = "",
) -> list[dict[str, str]]:
    """standing_lessons and retrieved_lessons are pre-formatted text blocks
    (harness.lessons.format_lessons()), empty by default so hill-climb
    (harness/loop.py, which never passes them) is unaffected — task 4.3's
    two-tier lesson injection is population-search-only, per PHASE-4.md's
    own per-generation/per-candidate framing.

    inspirations (task 3.4's cross-cell borrowing) has its own slot here,
    after the parent block, because that is where both PHASE-3.md's and
    PHASE-4.md's prompt-order diagrams put it: per-candidate, after the
    cache boundary. harness/generation.py used to splice it onto the end of
    task_description instead, which put per-candidate text in the invariant
    slot and meant nothing after the system prompt could be prefix-cached
    for any candidate that had inspirations. Found 2026-09-28 wiring task
    4.3, whose standing-lesson tier is worthless unless the region before
    the boundary is genuinely invariant."""
    user = USER_TEMPLATE.format(
        task_description=task_description,
        parent_block=parent_block,
        quality=quality,
        cost_tokens=cost_tokens,
        latency=latency,
        failed_checks=failed_checks,
        standing_lessons=standing_lessons,
        retrieved_lessons=retrieved_lessons,
        inspirations=inspirations,
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user},
    ]


def propose(
    task_description: str,
    parent_block: str,
    quality: float,
    cost_tokens: int,
    latency: float,
    failed_checks: str,
    temperature: float = 0.9,
    client: OpenAI | None = None,
    system_prompt: str = SYSTEM_PROMPT,
) -> tuple[str, int]:
    """One proposal call. Returns (raw response text, prompt+completion tokens).

    No lesson parameters — this is hill-climb's (harness/loop.py) sync
    path; task 4.3's lesson injection is population-search-only."""
    messages = _messages(task_description, parent_block, quality, cost_tokens, latency, failed_checks, system_prompt)
    r = (client or judge_client()).chat.completions.create(
        model="proposer",  # the LiteLLM role from Phase 0
        temperature=temperature,
        messages=messages,
    )
    text = r.choices[0].message.content or ""
    tokens = r.usage.total_tokens if r.usage else 0
    return text, tokens


_async_client: AsyncOpenAI | None = None
_async_client_loop = None


async def close_async_client() -> None:
    """Close the cached client inside the loop that created it. Called at the
    end of each generation's event loop; otherwise the client was garbage-
    collected after its loop closed and printed 'Event loop is closed'
    tracebacks into every run log (TODO.md decision 87). Harmless, but noise
    that looks like a failure."""
    global _async_client, _async_client_loop
    if _async_client is not None:
        try:
            await _async_client.close()
        finally:
            _async_client, _async_client_loop = None, None


def async_judge_client() -> AsyncOpenAI:
    """Async twin of harness.judge.judge_client(), same LiteLLM endpoint.
    See PHASE-3.md task 3.1 — this is what propose_many() fans out over.

    No timeout/max_retries override here left the SDK defaults (600s
    timeout, 2 retries — each re-applying that same 600s) — the same gap
    found live in harness.judge.judge_client() running capability_case's
    first real hill-climb, 2026-09-22, fixed there and mirrored here for
    consistency: 1200s matches litellm.config.yaml's own router timeout,
    and max_retries=0 avoids silently tripling the wait (and the GPU
    contention that caused the slowness) on a request that's still
    decoding, not failing.

    Cached per event loop, not per process. run_population runs each
    generation under its own asyncio.run, and a client created in one loop
    keeps pooled connections bound to it: the first request of the next
    generation reused one and failed with "Event loop is closed". Measured
    2026-10-18: exactly one propose_failed per generation, generations 1-9,
    always the generation's first proposal (TODO.md decision 77)."""
    global _async_client, _async_client_loop
    import asyncio

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None
    if _async_client is None or loop is not _async_client_loop:
        _async_client_loop = loop
        _async_client = AsyncOpenAI(
            base_url=os.environ.get("LITELLM_BASE_URL", "http://localhost:4000"),
            api_key=os.environ.get("LITELLM_API_KEY", "unused"),
            max_retries=0,
            timeout=1200.0,
        )
    return _async_client


async def propose_async(
    task_description: str,
    parent_block: str,
    quality: float,
    cost_tokens: int,
    latency: float,
    failed_checks: str,
    temperature: float = 0.9,
    client: AsyncOpenAI | None = None,
    system_prompt: str = SYSTEM_PROMPT,
    standing_lessons: str = "",
    retrieved_lessons: str = "",
    inspirations: str = "",
    capture: dict | None = None,
    model: str = "proposer",
) -> tuple[str, int, int]:
    """Async twin of propose(). See PHASE-3.md task 3.1 — this is what gets
    fanned out under a concurrency semaphore, not the sync version.

    Returns (text, total_tokens, completion_tokens). The aggregate-throughput
    figure this project has ever reported (the 437.8 tok/s from task 3.1,
    already flagged untrustworthy in TODO.md) was necessarily computed from
    total_tokens - prompt and completion combined - because that was the
    only number available. completion_tokens is real decode output, the
    quantity "tokens per second" actually means. Found needing a trustworthy
    number for PHASE-3.md's "aggregate throughput" Definition of Done line,
    2026-09-25.

    standing_lessons/retrieved_lessons: task 4.3's two-tier lesson
    injection, pre-formatted text blocks (harness.lessons.format_lessons()),
    empty by default.

    capture, if given, receives the exact messages sent and the model's
    reasoning (gpt-oss's analysis channel). PHASE-5.md task 5.1 trains on
    exactly this context, and the return shape stays as it is for every
    caller that does not need it.

    model is the LiteLLM role. PHASE-5.md task 5.4's paired A/B sends the
    same messages to "proposer" and "proposer-distilled"."""
    messages = _messages(
        task_description,
        parent_block,
        quality,
        cost_tokens,
        latency,
        failed_checks,
        system_prompt,
        standing_lessons,
        retrieved_lessons,
        inspirations,
    )
    r = await (client or async_judge_client()).chat.completions.create(
        model=model,
        temperature=temperature,
        messages=messages,
    )
    text = r.choices[0].message.content or ""
    tokens = r.usage.total_tokens if r.usage else 0
    completion_tokens = r.usage.completion_tokens if r.usage else 0
    if capture is not None:
        capture.update(messages=messages, reasoning=getattr(r.choices[0].message, "reasoning_content", None) or "")
    return text, tokens, completion_tokens
