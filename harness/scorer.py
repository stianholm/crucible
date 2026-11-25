"""The three-tier scorer. See PHASE-1.md task 1.4.

Order is cheapest first, deliberately. Phase 3 runs this sixty-four times
per generation, so a scorer that calls the judge before checking whether
the output even parses will dominate the compute budget with candidates
that were never viable.

Tier 1, gates — free, no model calls. Does it run, finish inside the wall
clock, and produce the right shape of output.

Tier 2, programmatic — cheap and deterministic. Most of the quality signal
should live here.

Tier 3, judged — expensive, only for candidates that cleared tier 1 and
only on tasks the adapter says need it.
"""

from __future__ import annotations

import statistics
import time

from harness.adapter import SolutionAdapter
from harness.fitness import Fitness
from harness.judge import score_with_judge
from harness.types import Task

# Bounds every adapter.invoke() call. Fine as a default — it's the parent-
# process backstop for a sandboxed subprocess (harness/sandbox.py already
# enforces its own in-container timeout well under this). It is NOT fine
# unmodified as a real network timeout for a solution whose invoke() makes
# an actual LLM call (capability_case): AGENTS.md's own documented rule is
# that client timeouts on this platform must exceed 15 minutes, since a
# single decode stream can drop to a few tokens/second under concurrency,
# and capability_case's own measured p50 latency (41.5s, uncontended) is
# already past this constant. Found by the session-review workflow,
# 2026-09-22. Fixed the same way as the rubric fallback below: an adapter
# can set eval_timeout_s to override this, evaluate() falls back to
# MAX_WALL_S when it doesn't.
MAX_WALL_S = 30.0

# Judge's share of quality when a task needs judgement at all. Kept out of
# the adapter contract deliberately — this is a scoring-policy knob, not a
# per-solution behaviour, and the default of 0 (programmatic checks only)
# is correct for any solution that never sets needs_judgement.
JUDGE_WEIGHT = 0.3


def task_class_of(adapter: SolutionAdapter, task: Task) -> str:
    """Which class a task belongs to for balanced scoring.

    Optional adapter hook, outside the frozen Protocol the way judge_view and
    rubric are. An adapter that does not define it puts every task in one class,
    which makes class_balanced_mean() identical to a plain mean - so `fixture`
    and `itot_classifier` are unaffected."""
    if hasattr(adapter, "task_class"):
        return adapter.task_class(task)
    return ""


def class_balanced_mean(adapter: SolutionAdapter, tasks: list[Task], qualities: list[float]) -> float:
    """Mean of per-class means, rather than a mean over tasks.

    A plain mean over tasks lets a constant policy score the majority class's
    share and never be caught. Measured on capability_case 2026-10-01: every arm
    A elite scored 0.00 on all nine must-reject held-out items and ~0.9 on the
    floor-passing ones, which a plain mean turns into 0.59 - and rotation's
    composition paid 0.61 for the same never-reject policy, so the search
    converged on it across multiple twenty-generation runs. Lesson memory moved
    it to the opposite corner, always-reject, scoring the must-reject share
    instead. Neither discriminates, and no Phase 3 or Phase 4 metric could see it
    because coverage, QD score, rotation scalar and held-out quality all move
    freely while the policy stays constant.

    Balanced, both degenerate corners cap near 0.5 by construction and only a
    candidate that actually discriminates can score above it."""
    by_class: dict[str, list[float]] = {}
    for task, q in zip(tasks, qualities):
        by_class.setdefault(task_class_of(adapter, task), []).append(q)
    if not by_class:
        return 0.0
    return statistics.mean(statistics.mean(v) for v in by_class.values())


def scorable(fitnesses: list[Fitness], tasks: list) -> tuple[list[Fitness], list]:
    """The (fitness, task) pairs that say something about the candidate.

    A judge_failed gate is the grader failing - a timeout, or a thinking loop
    that never reached a BAND line - not the candidate. Counting it as an
    invalid task threw the whole candidate out of the archive: across six
    capability_case ablation runs (TODO.md decision 66) 130 judge failures did
    exactly that, each to a candidate whose own output had passed its gates.
    It is missing data, so it is dropped from quality, validity and
    descriptors. Every other gate is the candidate's own failure and stays.
    If every task's judge failed there is nothing to score, so the inputs come
    back unchanged and the candidate stays invalid."""
    keep = [(f, t) for f, t in zip(fitnesses, tasks) if f.detail.get("gate") != "judge_failed"]
    if not keep:
        return list(fitnesses), list(tasks)
    return [f for f, _ in keep], [t for _, t in keep]


def stratified_sample(adapter: SolutionAdapter, tasks: list[Task], k: int, rng) -> list[Task]:
    """k tasks drawn to cover every class, proportionally where k allows.

    Balanced aggregation is useless if a candidate's sampled tasks all come from
    one class, which is what uniform sampling of k=3 from an imbalanced rotation
    does most of the time. Each class gets at least one slot; the remainder are
    allocated by class share."""
    by_class: dict[str, list[Task]] = {}
    for t in tasks:
        by_class.setdefault(task_class_of(adapter, t), []).append(t)
    if len(by_class) <= 1 or k <= 1:
        return [rng.choice(tasks) for _ in range(k)]

    classes = sorted(by_class)
    quota = {c: 1 for c in classes}
    for _ in range(max(0, k - len(classes))):
        # give the next slot to the class furthest below its proportional share
        target = max(classes, key=lambda c: len(by_class[c]) / len(tasks) - quota[c] / k)
        quota[target] += 1
    # Without replacement within a class, falling back to replacement only for
    # slots beyond the class's size. Until 2026-10-18 every slot was an
    # independent rng.choice, so a k=18 draw from capability_case's 33-task
    # rotation scored a candidate on 14 distinct tasks, repeating 4: repeats of
    # one task buy far less than new tasks when the worker is noisy per item
    # (TODO.md decisions 73, 78).
    out: list[Task] = []
    for c in classes:
        pool = by_class[c]
        q = quota[c]
        out += rng.sample(pool, min(q, len(pool))) + [rng.choice(pool) for _ in range(q - len(pool))]
    return out


def evaluate(
    adapter: SolutionAdapter,
    candidate_dir,
    task: Task,
    rubric: str | None = None,
) -> Fitness:
    t0 = time.perf_counter()
    timeout = getattr(adapter, "eval_timeout_s", MAX_WALL_S)

    # tier 1 — gates
    try:
        run = adapter.invoke(candidate_dir, task.input, timeout=timeout)
    except Exception as e:
        return Fitness(
            valid=False,
            quality=0.0,
            cost_tokens=0,
            latency_s=time.perf_counter() - t0,
            descriptors=(0, 0),
            detail={"gate": "raised", "error": repr(e)[:500]},
        )
    if run.output is None or not adapter.shape_ok(run.output):
        return Fitness(
            valid=False,
            quality=0.0,
            cost_tokens=run.tokens,
            latency_s=time.perf_counter() - t0,
            descriptors=(0, 0),
            detail={"gate": "shape", "got": str(run.output)[:500], "raw": run.raw},
        )

    # tier 2 — programmatic, deterministic, no model calls
    checks = adapter.programmatic_checks(run.output, task)
    prog = sum(p for p, _ in checks.values()) / len(checks) if checks else 0.0

    # tier 3 — judged, only where the adapter says a check cannot decide
    judged, judge_calls, judge_tokens, judge_completion_tokens = 1.0, 0, 0, 0
    if adapter.needs_judgement(task):
        # rubric is solution-specific, so the adapter is the natural owner
        # of it — falls back to adapter.rubric (an attribute outside the
        # frozen Protocol; existing adapters simply don't define it) if the
        # caller doesn't pass one explicitly. Neither loop.py nor
        # generation.py ever threaded an explicit rubric through — another
        # gap in a path nothing exercised before capability_case.
        if rubric is None:
            rubric = getattr(adapter, "rubric", None)
        if rubric is None:
            raise ValueError("adapter.needs_judgement(task) is True but no rubric was provided")
        # The judge grades what the candidate produced, not the task it was
        # given — task.input alone (no candidate output) was a latent bug,
        # never caught because no solution set needs_judgement True before
        # capability_case. Both are included: the judge needs the task for
        # context and the output to actually grade.
        #
        # run.output can itself have been shaped by untrusted, proposer-
        # evolved instructions (capability_case: the same judge-role model
        # executes the candidate, then grades what it just produced) — an
        # adapter can define judge_view(output) to control exactly what
        # reaches this second call, e.g. extracting only the structured
        # fields rather than passing the full raw response through
        # unsanitized. Falls back to the raw output for any adapter that
        # doesn't define one (current behaviour, unchanged). Found by the
        # session-review workflow, 2026-09-22.
        judge_view = adapter.judge_view(run.output) if hasattr(adapter, "judge_view") else run.output
        judge_prompt = f"## Task\n{task.input}\n\n## Candidate's response\n{judge_view}"
        # harness.judge.parse_band() deliberately raises when it can't find
        # a BAND line — "an unparseable response is a scorer bug, not a 0",
        # per its own docstring. True in general, but a real capability_case
        # hill-climb run hit a genuine exception to that: the judge-role
        # model can enter the same reasoning-loop failure mode documented in
        # BASELINE.yaml (burns the whole context window, never reaches
        # </think>) on the GRADING call itself, not just the worker call —
        # and nothing here caught it, so one bad judge response crashed the
        # entire multi-hour run. adapter.invoke() already handles its own
        # failures this way (a gate, not a crash); tier 3 needs the same
        # symmetry. Treated as invalid rather than a 0.0 judged score,
        # consistent with parse_band()'s own reasoning: a non-answer means
        # "couldn't determine", not "determined the candidate was bad" —
        # scoring it 0.0 would silently conflate the two. Found running
        # capability_case's first full-length hill-climb, 2026-09-23.
        try:
            judged, evidence, judge_calls, judge_tokens, judge_completion_tokens = score_with_judge(rubric, judge_prompt)
        except Exception as e:
            return Fitness(
                valid=False,
                quality=0.0,
                cost_tokens=run.tokens,
                latency_s=time.perf_counter() - t0,
                descriptors=(0, 0),
                detail={"gate": "judge_failed", "error": repr(e)[:500]},
            )
        checks["judge"] = (judged, evidence)

    quality = prog if judge_calls == 0 else (1 - JUDGE_WEIGHT) * prog + JUDGE_WEIGHT * judged

    return Fitness(
        valid=True,
        quality=quality,
        # run.tokens alone undercounted every judged solution's real cost —
        # the judge call's own tokens (judge_tokens, 0 when no judgement was
        # needed) never reached here before. Found by the session-review
        # workflow, 2026-09-22.
        cost_tokens=run.tokens + judge_tokens,
        latency_s=time.perf_counter() - t0,
        descriptors=adapter.descriptors(run),
        # completion_tokens (added 2026-09-25): run.raw's completion count
        # (0 for an adapter that doesn't set it - code-executing solutions
        # have no such concept) plus the judge call's own, for a trustworthy
        # aggregate-throughput figure. cost_tokens above stays
        # prompt+completion combined - it's a search objective (minimised),
        # not a throughput measurement, so the conflation there is harmless.
        detail={
            "checks": checks,
            "judge_calls": judge_calls,
            "completion_tokens": run.raw.get("completion_tokens", 0) + judge_completion_tokens,
        },
    )
