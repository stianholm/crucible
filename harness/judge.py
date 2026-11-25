"""Judge client and rubric plumbing. See PHASE-1.md task 1.4, "Judge discipline".

Five rules, each of which exists because breaking it produces scores that
look fine and mean nothing:
1. The judge model is never the proposer model.
2. Temperature zero, and a fixed rubric that is versioned and never evolved.
3. Score in small integer bands (0-3), not 0-100.
4. Calibrate once against ~30 human-labelled items before trusting it.
5. Return the judge's text as evidence — Phase 4 cannot reflect on a bare number.
"""

from __future__ import annotations

import os
import re

from openai import OpenAI

JUDGE_RUBRIC_VERSION = 1

_client: OpenAI | None = None


def judge_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(
            base_url=os.environ.get("LITELLM_BASE_URL", "http://localhost:4000"),
            api_key=os.environ.get("LITELLM_API_KEY", "unused"),
            # A timeout here means the model is genuinely still decoding
            # under load, not a transient error — the SDK default
            # (max_retries=2) would silently re-queue the same request up to
            # 3 times, each bound by the same timeout, multiplying both the
            # wait and the GPU contention that caused the slowness in the
            # first place. Fail once, fail fast. Found by the session-review
            # workflow, 2026-09-22.
            max_retries=0,
            # No timeout override here left the SDK default (600s), which a
            # real capability_case hill-climb run exceeded outright —
            # openai.APITimeoutError, uncaught, killed the whole run.
            # score_with_judge() never passed a per-call timeout, and this
            # client is also what harness.proposal.propose() (the sync
            # path, used by loop.py) reuses via its own client=None
            # default, so both call types shared the same gap. 1200s
            # matches litellm.config.yaml's own router timeout exactly —
            # the client-side and router-side ceilings now actually agree,
            # instead of the client giving up before the router does (the
            # same "one layer fixes it, the other doesn't" pattern the
            # session-review workflow already found for MAX_WALL_S).
            # Found live, 2026-09-22, running the first real hill-climb
            # against capability_case.
            timeout=1200.0,
        )
    return _client


def parse_band(text: str) -> int:
    """Extract a 0-3 integer band from the judge's response. Strict on
    purpose — an unparseable response is a scorer bug, not a 0."""
    m = re.search(r"\bBAND:\s*([0-3])\b", text)
    if not m:
        raise ValueError(f"could not parse a BAND: 0-3 from judge response: {text[:200]!r}")
    return int(m.group(1))


def score_with_judge(rubric: str, prompt: str) -> tuple[float, str, int, int, int]:
    """Score one item against a versioned rubric. Returns (score 0..1,
    evidence, judge_calls, tokens, completion_tokens).

    tokens was silently dropped before — r.usage was never read, so a
    judge call's real cost never reached Fitness.cost_tokens or any
    token budget. Invisible for every solution before capability_case,
    since none of them actually spent a judge call. Found by the
    session-review workflow, 2026-09-22.

    completion_tokens (added 2026-09-25) is the decode-only count, needed
    for a trustworthy aggregate-throughput figure — tokens above is
    prompt+completion combined, the same conflation already flagged
    elsewhere as making task 3.1's 437.8 tok/s untrustworthy."""
    r = judge_client().chat.completions.create(
        model="judge",  # the LiteLLM role from Phase 0
        temperature=0.0,
        messages=[
            {"role": "system", "content": rubric},
            {"role": "user", "content": prompt},
        ],
    )
    text = r.choices[0].message.content or ""
    band = parse_band(text)
    tokens = r.usage.total_tokens if r.usage else 0
    completion_tokens = r.usage.completion_tokens if r.usage else 0
    # A thinking model's <think> block can run past 1000 chars on its own —
    # reproduced live against the real judge model, 2026-09-22: a real
    # grading call's first 1000 chars fell entirely inside the think block,
    # containing no STEP 1, no STEP 2, and no BAND line at all. Stored
    # evidence must contain the judge's actual conclusion, not an arbitrary
    # mid-thought fragment, or rule 5 ("Phase 4 cannot reflect on a bare
    # number") is defeated. Strip the think block before truncating, and
    # give the remainder more room than the raw response ever needed
    # before a solution's rubric asked for multi-step reasoning. Found by
    # the session-review workflow, 2026-09-22.
    evidence_text = text.split("</think>", 1)[-1] if "</think>" in text else text
    return band / 3.0, evidence_text.strip()[:2000], 1, tokens, completion_tokens
