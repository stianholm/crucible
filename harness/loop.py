"""The hill-climb loop. See PHASE-2.md task 2.4.

One parent, one child, greedy accept — deliberately trivial, with one
subtlety worth the whole task: the noise ratchet. With a noisy metric and
a greedy accept rule, a single lucky draw becomes an incumbent whose
recorded score nothing can honestly beat. Re-evaluating on accept (two
extra evaluations, nothing in the budget) is the difference between a loop
that climbs and one that stalls after the first lucky accept.
"""

from __future__ import annotations

import hashlib
import statistics
from dataclasses import dataclass
from pathlib import Path

from harness.adapter import SolutionAdapter
from harness.budget import Budget
from harness.persistence import IterationWriter
from harness.proposal import SYSTEM_PROMPT, TEXT_SYSTEM_PROMPT, parse_candidate, propose
from harness.scorer import class_balanced_mean, evaluate, scorable
from harness.types import Task
from harness.validate import admissible


@dataclass
class AggregateScore:
    quality: float
    cost_tokens: float
    latency_s: float
    scalar: float
    failed_checks_text: str
    all_valid: bool


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def score_over(adapter: SolutionAdapter, cand_dir: Path, tasks: list[Task]) -> AggregateScore:
    fitnesses = [evaluate(adapter, cand_dir, t) for t in tasks]
    failed = []
    for t, f in zip(tasks, fitnesses):
        if not f.valid:
            # A tier-1 gate failure has no "checks" key in detail at all —
            # the loop below silently produced nothing for it, so a task
            # that failed catastrophically (an exception, an unparseable
            # response) was invisible in "where it lost points" even
            # though it zeroed the whole candidate's all_valid. Found
            # running a real capability_case hill-climb, 2026-09-22: a
            # gate failure (the judge-role model hit --max-model-len
            # mid-reasoning-loop, 15,467 tokens, never reached an answer)
            # sat completely unreported next to the one genuine
            # programmatic-check miss that did show up.
            gate = f.detail.get("gate", "unknown")
            raw = f.detail.get("raw") or {}
            # "raised" gate carries error at the top level; "shape" gate's
            # real error (if any) is one level down in raw, from
            # run_in_sandbox()'s stderr capture or an adapter's own
            # exception text — "got" alone is often just "None".
            why = (
                f.detail.get("error")
                or raw.get("stderr")
                or raw.get("error")
                or str(f.detail.get("got", ""))[:200]
            )
            failed.append(f"{t.task_id} [gate:{gate}]: {why}")
        elif f.quality < 1.0:
            for name, (score, evidence) in f.detail.get("checks", {}).items():
                if score < 1.0:
                    failed.append(f"{t.task_id} [{name}]: {evidence}")
    scored, scored_tasks = scorable(fitnesses, tasks)
    return AggregateScore(
        # Mean of per-class means, not a mean over tasks: a plain mean lets a
        # constant policy score the majority class's share. See
        # harness/scorer.py's class_balanced_mean for the measurement that
        # forced this. Identical to a plain mean for an adapter with no
        # task_class hook.
        # Judge failures are dropped as missing data - see scorer.scorable.
        quality=class_balanced_mean(adapter, scored_tasks, [f.quality for f in scored]),
        cost_tokens=statistics.mean(f.cost_tokens for f in fitnesses),
        latency_s=statistics.mean(f.latency_s for f in fitnesses),
        scalar=statistics.mean(f.scalar for f in scored),
        failed_checks_text="\n".join(failed[:15]) or "(none — all tasks passed)",
        all_valid=all(f.valid for f in scored),
    )


def hill_climb(
    adapter: SolutionAdapter,
    task_description: str,
    incumbent_block: str,
    rotation: list[Task],
    baseline_scalar: float,
    baseline_sigma: float,
    writer: IterationWriter,
    budget: Budget,
    temperature: float = 0.9,
) -> str:
    """Returns the final incumbent block (unchanged if nothing was accepted)."""
    incumbent = incumbent_block
    inc_score = baseline_scalar
    sigma = baseline_sigma
    rejects = 0
    last_score: AggregateScore | None = None
    # executes_code selects the evaluator (Phase 1) and, here, the proposal
    # wording too — a text artifact isn't "the body of a function".
    system_prompt = SYSTEM_PROMPT if adapter.executes_code else TEXT_SYSTEM_PROMPT

    for i in budget.iterations():
        cand_dir = adapter.materialise(incumbent)
        current = last_score or score_over(adapter, cand_dir, rotation)
        last_score = current

        text, tokens = propose(
            task_description=task_description,
            parent_block=incumbent,
            quality=current.quality,
            cost_tokens=int(current.cost_tokens),
            latency=current.latency_s,
            failed_checks=current.failed_checks_text,
            temperature=temperature,
            system_prompt=system_prompt,
        )
        budget.spend_tokens(tokens)

        cand = parse_candidate(text)
        if cand is None:
            writer.record(i, "parse_failed", parent_sha=sha(incumbent), prompt_tokens=tokens)
            rejects += 1
            if rejects >= budget.patience:
                break
            continue

        ok, why = admissible(cand, incumbent, adapter.materialise, max_growth=getattr(adapter, "max_growth", None))
        if not ok:
            writer.record(
                i,
                "inadmissible",
                parent_sha=sha(incumbent),
                candidate_sha=sha(cand),
                reason=why,
                prompt_tokens=tokens,
            )
            rejects += 1
            if rejects >= budget.patience:
                break
            continue

        parent_sha_val = sha(incumbent)  # captured before a possible reassignment below

        new_cand_dir = adapter.materialise(cand)
        agg = score_over(adapter, new_cand_dir, rotation)
        accepted = agg.all_valid and agg.scalar > inc_score + 2 * sigma

        if accepted:
            # defeat the noise ratchet: confirm with two more independent
            # evaluations before trusting a single lucky draw.
            confirms = [score_over(adapter, adapter.materialise(cand), rotation).scalar for _ in range(2)]
            mean_score = (agg.scalar + sum(confirms)) / 3
            if mean_score > inc_score + sigma:
                incumbent, inc_score, rejects = cand, mean_score, 0
                last_score = None  # force recompute of `current` against the new incumbent next iteration
            else:
                accepted = False

        writer.record(
            i,
            "scored",
            parent_sha=parent_sha_val,
            candidate_sha=sha(cand),
            candidate_block=cand,
            fitness=_fake_fitness(agg),
            accepted=accepted,
            prompt_tokens=tokens,
        )

        if not accepted:
            rejects += 1
        if rejects >= budget.patience:
            break

    return incumbent


def _fake_fitness(agg: AggregateScore):
    """IterationWriter.record() takes a harness.fitness.Fitness — this
    loop scores over a *set* of tasks and only has aggregate numbers, so
    wrap them in the same shape rather than widen the persistence API.

    Note: the persisted `scalar` column ends up being Fitness.scalar
    *recomputed from the mean* quality/cost_tokens/latency_s, not
    `agg.scalar` (the mean of the per-task scalars used for the actual
    accept decision above). These agree exactly as long as no individual
    task's cost/latency hits Fitness.scalar's internal min(x, 2.0) cap —
    true for this fixture (cost_tokens is always 0, latency stays well
    under the cap) but not guaranteed for every solution. If a future
    solution's persisted scalar ever looks inconsistent with its accept/
    reject outcome, this is where to look first.
    """
    from harness.fitness import Fitness

    return Fitness(
        valid=agg.all_valid,
        quality=agg.quality,
        cost_tokens=int(agg.cost_tokens),
        latency_s=agg.latency_s,
        descriptors=(0, 0),
        detail={"failed_checks": agg.failed_checks_text},
    )
