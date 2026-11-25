"""SolutionAdapter for capability_case. See PHASE-1.md task 1.1.

The first executes_code=False solution onboarded — the in-process
evaluator path PHASE-1.md always specified but nothing exercised until
now. invoke() makes a real model call (judge-role, temperature 0), no
sandbox: the candidate is instructions text, not code, so there is
nothing to contain the way harness.sandbox contains an executable
candidate.
"""

from __future__ import annotations

import json
import re
import tempfile
import time
from pathlib import Path
from typing import Any

from harness.judge import judge_client
from harness.types import Run, Task
from solutions.capability_case.checks.rubric import JUDGE_RUBRIC, VERDICTS

# What the proposer is told the component must do. One home for it, instead
# of a copy in every driver script.
#
# Extended 2026-10-18 (TODO.md decision 78) with the standard itself. Until
# then it named "Section 8" and "Section 9's anti-patterns" without stating
# them, and nearly every evolved candidate invented its own Section 9 list
# (control/data-plane separation, drift detection, ...), which the first
# harvest review found too pervasive to exclude. This is the specification the
# rubric in checks/rubric.py encodes, not any task's content.
TASK_DESCRIPTION = (
    "Whether a proposed capability case for relaxing per-action human approval on an "
    "operational-change gateway action is correctly judged sound, needs-more-evidence, or "
    "rejected outright, per Section 8 (Strategy C, capability-based opening) and Section 9's "
    "anti-patterns from the ITOT-boundary-as-architecture whitepaper.\n\n"
    "The standard, as the whitepaper states it. A case must be rejected if any of these hold: "
    "(1) evaluation runs only as a nightly batch instead of before each action (p.29); "
    "(2) governance for the relaxation is not defined upfront, 'we will govern it later' (p.29); "
    "(3) the case relies on the agent knowing when to stop rather than an independent "
    "architectural safeguard (p.28); "
    "(4) any of the four evidence dimensions is entirely absent: test results, failure-mode "
    "analysis, audit findings, comparison against the human-approved baseline (p.25). "
    "Evidence that is present but thin is not grounds for rejection: above this floor the "
    "choice between sound and needs-more-evidence is a judgment on how thin the evidence is. "
    "These are the only Section 9 anti-patterns; the whitepaper names no others."
)

OUTPUT_CONTRACT = (
    'Respond with exactly one JSON object, no other text: '
    '{"verdict": "sound" | "needs_more_evidence" | "reject", "reasoning": "..."}'
)

USER_TEMPLATE = "{narrative}\n\n" + OUTPUT_CONTRACT.replace("{", "{{").replace("}", "}}")

# Appended after the evolved instructions in the system message, so the
# harness, not the candidate, has the last word on output format. The
# contract used to live only in the user message, and evolved instructions
# routinely prescribe their own format ("first line: rejected", "Verdict:
# ...") which the worker then followed over the user turn on some calls and
# not others. Measured across six ablation runs (TODO.md decision 66): 923 of
# 9,225 task evaluations failed the shape gate, 920 of them plain text, and
# one failed task invalidates the whole candidate. Format is the harness's
# interface, not part of what is being evolved.
SYSTEM_SUFFIX = "\n\nOUTPUT FORMAT (overrides any format described above). " + OUTPUT_CONTRACT

_JSON_OBJECT = re.compile(r"\{.*\}", re.S)


def _parse_verdict(output: str) -> dict | None:
    """judge-role is a thinking model (Qwen3-4B) — it wraps its answer in
    a <think>...</think> block by default, so the raw response is never
    pure JSON even when the candidate's instructions ask for exactly that.
    Search past it rather than require compliance, the same way
    harness.judge.parse_band() searches for BAND: N anywhere in the text
    instead of requiring the whole response to be just that."""
    text = output.split("</think>", 1)[-1] if "</think>" in output else output
    m = _JSON_OBJECT.search(text)
    if not m:
        return None
    try:
        d = json.loads(m.group(0))
    except (ValueError, TypeError):
        return None
    return d if isinstance(d, dict) else None


class CapabilityCaseAdapter:
    solution_id = "capability_case"
    executes_code = False
    rubric = JUDGE_RUBRIC  # see harness/scorer.py — the adapter owns its rubric
    # invoke() is a real network call to a local LLM, not a bounded sandboxed
    # subprocess — harness/scorer.py's MAX_WALL_S (30s) is sized for the
    # latter. AGENTS.md's own documented rule: client timeouts on this
    # platform must exceed 15 minutes, since a single decode stream can drop
    # to a few tokens/second under concurrency. Measured p50 here is already
    # 41.5s uncontended (BASELINE.yaml) — 30s silently scored most real
    # calls as invalid. Found by the session-review workflow, 2026-09-22.
    eval_timeout_s = 900.0
    # harness/validate.py's default MAX_GROWTH (3.0) is sized for code,
    # where a 3x rewrite of a function body usually is bloat. This
    # solution's first real hill-climb run (2026-09-22) found every single
    # proposal across 12 iterations rejected as inadmissible, all "grew
    # Nx" (3.2x-5.7x): the incumbent is a genuinely short (676-char) prose
    # paragraph, and a correct rewrite covering four evidence dimensions
    # plus three anti-pattern checks legitimately needs to be several
    # times longer — that's a correct fix, not runaway growth. Set high
    # enough to comfortably allow real expansion while still catching
    # genuinely degenerate output (e.g. a repetition loop).
    max_growth = 15.0

    def materialise(self, block: str) -> Path:
        d = Path(tempfile.mkdtemp(prefix="capcase-cand-"))
        (d / "instructions.txt").write_text(block.strip("\n") + "\n")
        return d

    def invoke(self, cand: Path, task_input: str, timeout: float) -> Run:
        instructions = (cand / "instructions.txt").read_text()
        scenario = json.loads(task_input)
        t0 = time.perf_counter()
        try:
            r = judge_client().chat.completions.create(
                # The WORKER role, changed from "judge" to "proposer" 2026-10-05.
                #
                # This does not breach PHASE-1.md's judge discipline rule 1. That
                # rule constrains the *grader* ("the judge model is never the
                # proposer model", because a model grades its own output
                # generously); it says nothing about which model executes the
                # candidate. The comment this replaces read it as constraining
                # the worker, which is not what the rule says. Grading still
                # happens on the judge role, in harness/scorer.py.
                #
                # It also closes the rule-1 gap PHASE-1.md documents and
                # explicitly left unsolved: for an executes_code:false solution
                # the executor and grader were literally the same model, so the
                # rule's letter held and its purpose did not. Now they differ.
                #
                # Measured reason for the change. Qwen3-4B cannot execute this
                # solution's conditional rule, and every search result before
                # this was that limitation rather than a property of the task.
                # Same candidates, judge-role worker against proposer-role
                # worker, balanced held-out quality: hand-written reference
                # 0.474 -> 0.652, incumbent 0.489 -> 0.500. And one generation of
                # search under the new worker produced a candidate at 0.688
                # must_reject / 0.700 floor_pass, balanced 0.694 - the first
                # genuinely discriminating candidate this solution has ever
                # produced, where 20+ generations on the judge role never
                # exceeded 0.51 and sat at never-reject or always-reject.
                #
                # It is also cheaper, which inverts the affordability assumption
                # that drove the original wiring: 425.6s per generation against
                # ~1,400s, and 195k tokens against ~208k. Qwen3-4B runs at
                # --gpu-memory-utilization 0.09 and has too little KV cache to
                # sustain 16-way concurrency; gpt-oss-120b at 0.74 sustains 32.
                # No third model is added, so docs/platform.md's budget is unchanged.
                model="proposer",
                temperature=0.0,
                messages=[
                    {"role": "system", "content": instructions + SYSTEM_SUFFIX},
                    {"role": "user", "content": USER_TEMPLATE.format(narrative=scenario["narrative"])},
                ],
                timeout=timeout,
            )
        except Exception as e:
            return Run(
                output=None,
                tokens=0,
                tool_calls=0,
                wall_time_s=time.perf_counter() - t0,
                raw={"stderr": repr(e)[:2000]},
            )
        text = r.choices[0].message.content or ""
        tokens = r.usage.total_tokens if r.usage else 0
        # completion_tokens (2026-09-25): decode-only count, needed for a
        # trustworthy aggregate-throughput figure - tokens above is
        # prompt+completion combined. Stashed in raw rather than added to
        # Run's frozen fields, matching Fitness.detail's existing pattern.
        completion_tokens = r.usage.completion_tokens if r.usage else 0
        return Run(
            output=text.strip(),
            tokens=tokens,
            tool_calls=0,
            wall_time_s=time.perf_counter() - t0,
            raw={"completion_tokens": completion_tokens},
        )

    def shape_ok(self, output: Any) -> bool:
        if not isinstance(output, str):
            return False
        d = _parse_verdict(output)
        return d is not None and d.get("verdict") in VERDICTS and isinstance(d.get("reasoning"), str)

    def judge_view(self, output: str) -> str:
        """What the tier-3 judge call actually sees of the candidate's
        output — the extracted {verdict, reasoning} only, not the full raw
        response. The candidate's own instructions (untrusted, proposer-
        evolved) shaped that raw response via a call to this same judge-
        role model; passing it through unsanitized would let a candidate
        append text after the JSON that the grading call reads as part of
        the same turn, with nothing marking it as data rather than
        instructions. This doesn't make injection impossible — text
        embedded inside the reasoning field itself still reaches the judge
        — but it closes the most direct vector, and JUDGE_RUBRIC's own
        instructions (see checks/rubric.py) now tell the judge to treat
        anything that reads as an instruction, wherever it appears, as
        disqualifying rather than something to follow. Found by the
        session-review workflow, 2026-09-22."""
        d = _parse_verdict(output) or {}
        return json.dumps({"verdict": d.get("verdict"), "reasoning": d.get("reasoning")})

    def programmatic_checks(self, output: Any, task: Task) -> dict[str, tuple[float, str]]:
        got = _parse_verdict(output)
        verdict = got["verdict"]
        must_reject = task.expected["must_reject"]
        if must_reject:
            ok = verdict == "reject"
            evidence = f"floor requires reject ({'; '.join(task.expected['reasons'])}); got {verdict!r}"
        else:
            ok = verdict in ("sound", "needs_more_evidence")
            evidence = f"floor passes (no disqualifier); got {verdict!r} — 'reject' would be wrong here"
        return {"floor_correct": (1.0 if ok else 0.0, evidence)}

    def task_class(self, task: Task) -> str:
        """Two classes, for harness/scorer.py's class_balanced_mean.

        Without this the fitness averaged must-reject and floor-passing accuracy
        into one number, and a candidate that simply never said "reject" scored
        the floor-passing share: 0.61 on rotation, 0.59 on held-out. Measured
        2026-10-01, that is exactly what multiple twenty-generation searches
        converged on - every arm A elite scored 0.00 on all nine must-reject
        held-out items - while lesson memory converged on the opposite constant,
        always-reject. Neither discriminates, and no archive or quality metric
        could see it.

        Balanced, a constant policy caps near 0.5 and only real discrimination
        scores above it."""
        return "must_reject" if task.expected["must_reject"] else "floor_pass"

    def needs_judgement(self, task: Task) -> bool:
        # only floor-passing scenarios have real ambiguity worth a judge
        # call — floor-failing ones are already fully decided mechanically.
        return not task.expected["must_reject"]

    def descriptors(self, run: Run) -> tuple[int, int]:
        """Archive coordinates: reasoning length bin, latency bin. Not optimised.

        latency_bin was `min(int(wall_time_s), 5)` — a bucket width of one
        second, sized for a sub-second sandboxed run. Real calls here take
        ~15-90s (BASELINE.yaml: p50 41.5s), so that saturated to 5 for
        virtually every candidate, collapsing this axis of the archive grid
        to one usable cell out of six. Found by the session-review
        workflow, 2026-09-22. Fixed the same way itot_classifier's
        runtime_bin scales for its own measured range: 15s-wide buckets, so
        the axis actually spans the range this solution really produces.
        """
        d = _parse_verdict(run.output or "") or {}
        reasoning = d.get("reasoning", "")
        length_bin = min(len(reasoning) // 200, 5)
        latency_bin = min(int(run.wall_time_s // 15), 5)
        return (length_bin, latency_bin)
