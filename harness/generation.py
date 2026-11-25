"""One generation of population search. Ties together task 3.1
(concurrent proposing), 3.2 (archive), 3.3 (islands), 3.4 (parent
selection), and 3.5 (the sandbox pool). See PHASE-3.md.

Carried over unchanged from Phase 2, per the phase's own handoff note:
the proposal contract and its parser, the validation ladder, the sandbox
runner and its abuse suite, the two-sigma significance test. Only the
search strategy — one parent to archive-driven selection across islands —
changes this phase.
"""

from __future__ import annotations

import asyncio
import hashlib
import random
import statistics
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from psycopg.types.json import Jsonb

from harness.adapter import SolutionAdapter
from harness.archive import cells, try_insert
from harness.fitness import Fitness
from harness.islands import N_ISLANDS, migrate, should_migrate
from harness.persistence import IterationWriter
from harness.scorer import class_balanced_mean, scorable
from harness.proposal import SYSTEM_PROMPT, TEXT_SYSTEM_PROMPT, parse_candidate, propose_async
from harness.sandbox_pool import SandboxPool
from harness.selection import inspirations, select_parents
from harness.types import Task
from harness.validate import admissible


# Headings for task 4.3's two lesson tiers, as they appear in the proposal
# prompt (harness/proposal.py's USER_TEMPLATE slots).
STANDING_HEADING = "Lessons from past failures"
RETRIEVED_HEADING = "Lessons relevant to this version's failures"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def _root_sha_for(parent: dict, cand: str) -> str:
    """The lineage ancestor a new candidate descends from. An elite parent
    already carries one (root_sha), propagated unchanged. A parent fresh
    from the seed (root_sha None — nothing claimed in this island yet) has
    no ancestor of its own, so the new candidate becomes its own root: each
    of generation 0's distinct candidates is a separate founding lineage,
    not a clone of the shared seed.

    Falling back to sha(parent_block) instead (the seed's own hash, shared
    by every generation-0 candidate since they all share the same parent)
    made every run's unique_ancestors read exactly 1 forever, regardless of
    how diverse the search actually was — found from real Postgres data
    after this project's first 20-generation run, 2026-09-24; no test had
    ever exercised more than one generation before."""
    return parent.get("root_sha") or sha(cand)


@dataclass
class GenerationResult:
    generation: int
    n_candidates: int
    n_parsed: int
    n_admissible: int
    n_scored: int
    n_claimed: int  # newly claimed or improved archive cells
    completion_tokens: int = 0  # decode-only, proposal + evaluation - see "Aggregate throughput"
    migration_log: list[dict] = field(default_factory=list)
    newly_claimed: list[dict] = field(default_factory=list)  # for the report's "content" section


async def _propose_for_parent(
    task_description: str,
    parent: dict,
    inspiration_blocks: list[str],
    seed_block: str,
    temperature: float,
    sem: asyncio.Semaphore,
    system_prompt: str = SYSTEM_PROMPT,
    standing: list | None = None,
    retrieved: list | None = None,
    model: str = "proposer",
) -> tuple[dict, str, int, int, list, dict]:
    """standing/retrieved are task 4.3's two lesson tiers as Lesson lists.

    The sixth return value is the proposal as sent and received: messages,
    response text and reasoning. Stored on the iteration row, see
    persistence.py's `proposal` column.

    The fifth return value is the lessons this proposal actually carried,
    both tiers together, after the budget trim. The caller cannot work that
    out for itself, which is the whole reason it comes back from here: the
    retrieved tier is trimmed against this candidate's own prompt length.

    standing arrives already capped for the whole generation and is only
    formatted here, so the block is byte-identical for every candidate.
    retrieved is capped here, against this candidate's own prompt, because
    that is the first point the full per-candidate text exists. None for
    both (the default) is the pre-task-4.3 behaviour, and what every
    solution without a fitted taxonomy gets."""
    parent_block = parent["block"] if "block" in parent else seed_block
    inspiration_text = ""
    if inspiration_blocks:
        inspiration_text = "## Other solutions worth drawing from\n" + "\n\n".join(
            f"<inspiration>\n{b}\n</inspiration>" for b in inspiration_blocks
        )
    failed_checks = f"scalar {parent.get('scalar', 0.0):.3f} — try a genuinely different approach, not a copy"

    standing_text = retrieved_text = ""
    injected: list = []
    if standing or retrieved:
        from harness.lessons import apply_budget, format_lessons

        # "Roughly fifteen percent of the prompt" (PHASE-4.md task 4.3)
        # measured against the whole prompt, system message included, not
        # the user message alone - the system prompt is a third of what gets
        # sent for a text solution, and excluding it would tighten the real
        # cap to about half of what the phase document asks for.
        #
        # Only the retrieved tier is trimmed here. apply_budget()'s standing
        # return is deliberately discarded: the standing tier was already
        # capped once for the whole generation (see _standing_within_budget),
        # and trimming it again against this candidate's own prompt length
        # would make the supposedly-invariant block a different length for
        # every candidate. That is what this wiring first did, and it cut the
        # shared prefix from the whole cached region down to 287 characters -
        # a handful of tokens over the cap on a small prompt is far cheaper
        # than 64 candidates each re-prefilling a prefix that no longer
        # matches.
        _standing_ignored, kept_retrieved = apply_budget(
            system_prompt + task_description + inspiration_text + parent_block + failed_checks,
            standing or [],
            retrieved or [],
        )
        standing_text = format_lessons(standing or [], STANDING_HEADING)
        retrieved_text = format_lessons(kept_retrieved, RETRIEVED_HEADING)
        injected = list(standing or []) + list(kept_retrieved)

    capture: dict = {}
    async with sem:
        text, tokens, completion_tokens = await propose_async(
            task_description=task_description,
            inspirations=inspiration_text,
            parent_block=parent_block,
            quality=parent.get("scalar", 0.0),
            cost_tokens=0,
            latency=0.0,
            failed_checks=failed_checks,
            temperature=temperature,
            system_prompt=system_prompt,
            standing_lessons=standing_text,
            retrieved_lessons=retrieved_text,
            capture=capture,
            model=model,
        )
    return parent, text, tokens, completion_tokens, injected, capture | {"content": text}


def _taxonomy_context(sol_dir: Path | None) -> tuple[object | None, list]:
    """The fitted vectorizer and failure categories, loaded whenever a taxonomy
    exists, independent of whether lessons are injected.

    Separate from _lesson_context because categorising a failure and acting on a
    lesson are different jobs. They were conflated, and the cost was task 4.5's
    control arm: a lessons-off run recorded no failure_id or failure_ids, so
    task 4.6's metrics could only ever be computed for the treatment arm."""
    if sol_dir is None:
        return None, []
    pkl, yml = sol_dir / "taxonomy_vectorizer.pkl", sol_dir / "taxonomy.yaml"
    if not (pkl.exists() and yml.exists()):
        return None, []
    from harness.taxonomy import load_taxonomy

    categories, vectorizer = load_taxonomy(yml, pkl)
    return vectorizer, categories


def _lesson_context(sol_dir: Path | None, conn, solution_id: str) -> tuple[object | None, list, list, list]:
    """Task 4.3's once-per-generation load: the fitted TF-IDF vectorizer
    (what per-candidate retrieval needs), the active lesson list
    (retrieval's corpus), the standing lessons (the same list for every
    candidate in this generation), and the task 4.1 failure categories the
    vectorizer was fitted alongside.

    The categories are what closes the falsification loop. A lesson is
    admitted against one category (Lesson.failure_id), so asking whether the
    lesson worked means asking whether that category reappeared in the
    child's own failure evidence, which needs the centroids to assign
    against.

    The standing tier is loaded once here but formatted per candidate, in
    _propose_for_parent, because the budget trim (harness.lessons.
    apply_budget) needs that candidate's own non-lesson prompt text before
    it knows how much of the tier fits.

    Returns the empty context rather than raising for a solution with no
    taxonomy fitted yet (fixture, itot_classifier) or no admitted lessons
    yet. Those must still search exactly as they did before task 4.3.

    Two queries, not one, so harness.lessons.standing_lessons() stays the
    single definition of which lessons are standing. Both run once per
    generation against a table of tens of rows, not per candidate."""
    if sol_dir is None:
        return None, [], [], []
    from harness.lessons import active_lessons, standing_lessons

    vectorizer, categories = None, []
    pkl, yml = sol_dir / "taxonomy_vectorizer.pkl", sol_dir / "taxonomy.yaml"
    if pkl.exists() and yml.exists():
        from harness.taxonomy import load_taxonomy

        categories, vectorizer = load_taxonomy(yml, pkl)

    return vectorizer, active_lessons(conn, solution_id), standing_lessons(conn, solution_id), categories


def _aggregate_fitness(fitnesses: list, tasks: list, adapter=None) -> tuple[Fitness, int]:
    """One Fitness per candidate out of its several per-task evaluations,
    plus that candidate's true total token spend.

    Scoring each candidate on a single sampled task made archive placement
    turn substantially on which task a candidate happened to draw: two
    candidates were compared on different tasks, and try_insert() ranks them
    against each other on those numbers. Measured 2026-09-28, it also starved
    task 4.3's retrieved lesson tier, because a candidate that passes its one
    task produces no failure evidence to retrieve against and 47 of 54 elites
    had none.

    Aggregation follows harness/loop.py's score_over(), which is this
    project's existing multi-task aggregate and what generation.py's own
    comment called the affordable choice: mean quality, mean cost, mean
    latency, valid only if every task was valid.

    Cost is the mean, not the sum, for two reasons. Fitness.scalar penalises
    cost against a 4,000-token anchor, so a sum would saturate every
    candidate's cost penalty and leave quality as the only differentiator;
    and score_over() already means it, so hill-climb and population-search
    scalars stay comparable. The sum is returned separately because the
    budget has to see real spend - recording the mean in the iteration row
    would undercount a generation by a factor of k, which is the same class
    of bug as decision 30's token undercount.

    Descriptors are the per-axis median, which is the point of the change:
    an archive cell should describe the candidate, not one task's luck.

    detail carries every task's evidence with the task id prefixed onto the
    check name, so harness/taxonomy.py's extract_evidence() sees all of it
    through the shape it already expects. A task that failed its gate is
    recorded as a failed check rather than a top-level "gate" key, since
    only one such key can survive a merge and its evidence would otherwise
    be dropped."""
    task_ids = [getattr(t, "task_id", t) for t in tasks]
    checks: dict[str, tuple[float, str]] = {}
    completion_tokens = 0
    for fitness, task_id in zip(fitnesses, task_ids):
        completion_tokens += fitness.detail.get("completion_tokens", 0)
        if "gate" in fitness.detail:
            why = fitness.detail.get("error") or str(fitness.detail.get("got", ""))
            checks[f"{task_id}/gate:{fitness.detail['gate']}"] = (0.0, why or f"gate {fitness.detail['gate']}")
            continue
        for name, (score, evidence) in (fitness.detail.get("checks") or {}).items():
            checks[f"{task_id}/{name}"] = (score, evidence)

    # Judge failures are missing data, not candidate failures - see scorer.scorable.
    # Cost still counts every task, since those tokens were really spent.
    scored, scored_tasks = scorable(fitnesses, tasks)
    aggregate = Fitness(
        valid=all(f.valid for f in scored),
        # Class-balanced, matching harness/loop.py's score_over: a plain mean
        # over tasks lets a constant policy score the majority class's share.
        # Falls back to a plain mean when no adapter is given (the tests) or
        # when the adapter has no task_class hook.
        quality=(
            class_balanced_mean(adapter, scored_tasks, [f.quality for f in scored])
            if adapter is not None
            else statistics.mean(f.quality for f in scored)
        ),
        cost_tokens=round(statistics.mean(f.cost_tokens for f in fitnesses)),
        latency_s=statistics.mean(f.latency_s for f in fitnesses),
        descriptors=(
            round(statistics.median(f.descriptors[0] for f in scored)),
            round(statistics.median(f.descriptors[1] for f in scored)),
        ),
        detail={"checks": checks, "completion_tokens": completion_tokens, "n_tasks": len(fitnesses)},
    )
    return aggregate, sum(f.cost_tokens for f in fitnesses)


def _failure_categories(fitness, vectorizer, categories: list) -> tuple[str | None, set[str]]:
    """The task 4.1 categories this candidate's own failure evidence falls
    into, as (dominant, all of them).

    Each evidence item is assigned separately rather than assigning one
    joined blob, because a candidate that failed three checks can have
    failed them for three different reasons, and the falsification question
    below is asked per lesson. The dominant one is what goes in
    `iteration.failure_id`, which PHASE-4.md task 4.6's repeat-failure-rate
    SQL reads as a single value per row."""
    if vectorizer is None or not categories:
        return None, set()
    from harness.taxonomy import assign, extract_evidence

    found = []
    for item in extract_evidence([fitness.detail], [None]):
        category_id, _similarity = assign(item.text, vectorizer, categories)
        if category_id:
            found.append(category_id)
    if not found:
        return None, set()
    return Counter(found).most_common(1)[0][0], set(found)


def _record_lesson_outcome(
    conn, solution_id: str, run_id, n: int, fitness, injected: list, vectorizer, categories: list
) -> None:
    """Task 4.3's falsification step, and the thing that makes the lesson
    store a loop rather than a write-only log.

    A lesson is admitted against exactly one failure category, so asking
    whether it worked means asking whether that category reappeared in the
    evidence of the candidate the lesson was injected into. Absent means
    avoided, which is what `lesson.followed_ok` counts and what
    retire_underperforming() divides by `followed` to decide retirement.

    Deliberately only called for candidates that were actually evaluated. A
    proposal that failed to parse or was ruled inadmissible never contacted
    the rotation, so there is no evidence about whether its lessons helped,
    and counting it either way would corrupt the ratio retirement reads."""
    dominant, all_categories = _failure_categories(fitness, vectorizer, categories)
    with conn.cursor() as cur:
        cur.execute(
            "update iteration set failure_id = %s, failure_ids = %s, lessons_injected = %s "
            "where solution_id = %s and run_id = %s and n = %s",
            (
                dominant,
                sorted(all_categories) or None,
                [lesson.id for lesson in injected] or None,
                solution_id,
                run_id,
                n,
            ),
        )
    conn.commit()

    from harness.lessons import record_usage

    # Scored against the full category set on both sides. The control group is
    # read from `iteration.failure_ids`, which now holds the same set, so a
    # recurrence counts the same way whether or not the candidate received the
    # lesson.
    #
    # This was briefly compared on the dominant category alone, as the only
    # symmetric option available while a run was in flight and the
    # `failure_ids` column could not be added without taking an ACCESS
    # EXCLUSIVE lock on `iteration`. Before that it was asymmetric - full set
    # for the treated candidate, dominant category for the control - which
    # biased every lesson toward retirement.
    for lesson in injected:
        record_usage(conn, lesson.id, avoided_failure=lesson.failure_id not in all_categories)


def _standing_within_budget(standing: list, invariant_text: str) -> list:
    """Caps the standing tier once for the whole generation, against the
    invariant region of the prompt (system rules plus task description)
    rather than any one candidate's full prompt.

    Sizing it per candidate instead would give the tier a different length
    for every candidate, which defeats the only reason PHASE-4.md puts it
    before the cache boundary in the first place."""
    if not standing:
        return []
    from harness.lessons import apply_budget

    kept, _ = apply_budget(invariant_text, standing, [])
    return kept


def _parent_failure_text(conn, iteration_id: int | None) -> str:
    """The parent's own recorded failure evidence, as one blob to retrieve
    lessons against. Reuses harness.taxonomy.extract_evidence() so the text
    being matched has the same shape the vectorizer was fitted on - one
    snippet per failed check or gate failure - rather than some other
    serialisation of the same detail dict.

    A parent with no iteration_id (a seed parent, generation 0) or no
    recorded detail retrieves nothing, and gets the standing tier only."""
    if iteration_id is None:
        return ""
    with conn.cursor() as cur:
        cur.execute("select detail from iteration where id = %s", (iteration_id,))
        row = cur.fetchone()
    if not row or not row[0]:
        return ""
    from harness.taxonomy import extract_evidence

    return "\n".join(item.text for item in extract_evidence([row[0]], [None]))


async def run_generation(
    adapter: SolutionAdapter,
    task_description: str,
    seed_block: str,
    solution_id: str,
    generation: int,
    rotation: list[Task],
    writer: IterationWriter,
    pool: SandboxPool,
    candidates_per_island: int = 16,
    n_islands: int = N_ISLANDS,
    grid_dims: tuple[int, int] = (6, 6),
    knee_concurrency: int = 32,
    temperature: float = 0.9,
    rng: random.Random | None = None,
    sol_dir: Path | None = None,
    tasks_per_candidate: int = 1,
    taxonomy_only_dir: Path | None = None,
    proposer_models: tuple[str, ...] = ("proposer",),
) -> GenerationResult:
    """proposer_models with more than one entry is PHASE-5.md task 5.4's
    paired A/B: every selected parent is proposed from once per model, with
    byte-identical prompts, and all of the generation's candidates are scored
    on the same sampled tasks. See _expand_arms.

    sol_dir is where task 4.3's lesson injection finds the solution's
    fitted taxonomy vectorizer (taxonomy_vectorizer.pkl). None - the
    default - means no lesson injection at all, which is both what the
    tests pass and the correct behaviour for a solution that has never had
    a taxonomy built (fixture, itot_classifier)."""
    rng = rng or random.Random()
    conn = writer.conn

    # 0. lesson context, loaded once for the whole generation (task 4.3).
    # system_prompt is resolved here rather than at the proposal step below
    # because the standing tier's budget is measured against it.
    system_prompt = SYSTEM_PROMPT if adapter.executes_code else TEXT_SYSTEM_PROMPT
    # Categorising failures and injecting lessons are separate concerns, and
    # conflating them cost the ablation its control arm. sol_dir=None turns off
    # injection (task 4.5's arm A), but it was also turning off the taxonomy
    # load, so arm A recorded no failure_id or failure_ids at all - leaving
    # task 4.6's repeat-failure rate and per-category intensity computable for
    # the treatment arm only. Found 2026-10-06 after a ten-generation run with
    # lessons off produced 644 evidence items and zero categorised rows.
    #
    # taxonomy_dir therefore loads the vectorizer and categories whenever a
    # fitted taxonomy exists, regardless of whether lessons are injected.
    taxonomy_dir = sol_dir if sol_dir is not None else taxonomy_only_dir
    vectorizer, categories = _taxonomy_context(taxonomy_dir)
    _unused_vec, lessons, standing, _unused_cats = _lesson_context(sol_dir, conn, solution_id)
    standing = _standing_within_budget(standing, system_prompt + task_description)
    # Retrieval searches only lessons the standing tier is not already
    # carrying. Searching all of them put the highest-support lesson in both
    # blocks of the same prompt, wasting the tokens and, worse, calling
    # record_usage() twice for it, so its `followed` count grew at double
    # rate and its avoidance ratio was measured against an inflated
    # denominator. Found reading the first generation where retrieval
    # actually fired, 2026-09-29: the injected sets came back as [1, 4, 1, 5].
    standing_ids = {lesson.id for lesson in standing}
    retrievable = [lesson for lesson in lessons if lesson.id not in standing_ids]

    # 1. select parents across all islands (task 3.4)
    all_parents: list[tuple[int, dict, list[str], list]] = []  # island_id, parent, inspirations, retrieved lessons
    for island_id in range(n_islands):
        occupied = cells(conn, solution_id, island_id)
        parents = select_parents(conn, solution_id, island_id, candidates_per_island, grid_dims, seed_block, rng)
        for p in parents:
            if "block" not in p:
                # an elite dict from archive.cells() carries candidate_sha,
                # not the block text itself — fetch it from storage.
                p = dict(p)
                p["block"] = _fetch_block(p.get("candidate_sha")) or seed_block
            insp = inspirations(occupied, p.get("iteration_id"), k=2)
            insp_blocks = [b for c in insp if (b := _fetch_block(c.get("candidate_sha")))]
            # per-candidate lesson retrieval (task 4.3), against this
            # parent's own failure evidence - no model call, just cosine
            # similarity in the taxonomy's TF-IDF space.
            retrieved: list = []
            if vectorizer is not None and retrievable:
                from harness.lessons import retrieve_lessons

                retrieved = retrieve_lessons(
                    _parent_failure_text(conn, p.get("iteration_id")), vectorizer, retrievable
                )
            all_parents.append((island_id, p, insp_blocks, retrieved))

    # Close the read transaction before the proposal fan-out. Steps 0 and 1
    # are all reads, and psycopg opens a transaction on the first of them,
    # which then stayed open across step 2 - ten to twenty minutes of pure
    # network I/O waiting on the proposer - because nothing writes until the
    # scoring loop. Measured idle-in-transaction for 824 seconds on
    # 2026-09-29.
    #
    # An open transaction that long blocks vacuum, and it makes any concurrent
    # DDL wait; a waiting ACCESS EXCLUSIVE lock then queues every later reader
    # behind it, including this same connection's next statement. That is how a
    # read-only task 4.6 metrics query nearly stalled a ten-generation run.
    # Task 4.6 is meant to be readable *during* a run, so this window has to
    # close.
    #
    # Everything after this point commits as it goes: _set_generation_fields(),
    # _record_lesson_outcome() and try_insert() each commit their own work.
    conn.commit()

    # 1b. the A/B split (task 5.4): one slot per parent per proposer model.
    # Labels are resolved first, so a missing adapter stops the generation
    # before any request is sent.
    labels = {m: _model_label(m) for m in proposer_models}
    slots = _expand_arms(all_parents, proposer_models, rng)
    ab = len(proposer_models) > 1

    # 2. propose concurrently, semaphore-limited to the knee (task 3.1)
    sem = asyncio.Semaphore(knee_concurrency)
    results = await asyncio.gather(
        *(
            _propose_for_parent(
                task_description,
                p,
                insp_blocks,
                seed_block,
                temperature,
                sem,
                system_prompt,
                standing,
                retrieved,
                model,
            )
            for _, p, insp_blocks, retrieved, model, _pair in slots
        ),
        return_exceptions=True,
    )

    n_parsed = n_admissible = n_scored = n_claimed = 0
    newly_claimed = []
    completion_tokens_total = 0  # decode-only, across proposal + evaluation - see task 3.1's "Aggregate throughput"
    # island_id, parent, cand_dir, cand_block, tokens, injected lessons, proposal, (label, pair)
    to_evaluate: list[tuple[int, dict, Path, str, int, list, dict, tuple]] = []

    for (island_id, parent, _insp, _retrieved, model, pair), result in zip(slots, results):
        arm = (labels[model], pair if ab else None)
        if isinstance(result, Exception):
            n = _next_n(writer)
            writer.record(
                n,
                "propose_failed",
                reason=repr(result)[:500],
                candidate_sha=None,
            )
            _set_arm(conn, writer, n, arm)
            continue
        _parent, text, tokens, completion_tokens, injected, proposal = result
        completion_tokens_total += completion_tokens
        cand = parse_candidate(text)
        if cand is None:
            n = _next_n(writer)
            writer.record(n, "parse_failed", prompt_tokens=tokens)
            _store_proposal(conn, writer, n, proposal)
            _set_arm(conn, writer, n, arm)
            continue
        n_parsed += 1

        parent_block = parent.get("block", seed_block)
        ok, why = admissible(cand, parent_block, adapter.materialise, max_growth=getattr(adapter, "max_growth", None))
        if not ok:
            n = _next_n(writer)
            writer.record(
                n,
                "inadmissible",
                parent_sha=sha(parent_block),
                candidate_sha=sha(cand),
                reason=why,
                prompt_tokens=tokens,
            )
            _store_proposal(conn, writer, n, proposal)
            _set_arm(conn, writer, n, arm)
            continue
        n_admissible += 1

        cand_dir = adapter.materialise(cand)
        to_evaluate.append((island_id, parent, cand_dir, cand, tokens, injected, proposal, arm))

    # 3. evaluate concurrently across the sandbox pool (task 3.5), each
    # candidate over several rotation tasks, and the SAME tasks for every
    # candidate in the generation.
    #
    # This used to draw one task per candidate, independently. Two separate
    # problems with that, both measured 2026-09-28. Candidates were ranked
    # against each other by try_insert() on scores from different tasks, so
    # archive placement turned substantially on which task a candidate
    # happened to draw. And a candidate that passed its single task produced
    # no failure evidence at all, which starved task 4.3's retrieved lesson
    # tier so completely that across 32 candidates not one received a
    # retrieved lesson (47 of 54 elites carried no evidence).
    #
    # Sampling the tasks once per generation rather than once per candidate
    # is what makes the comparison fair; evaluating more than one is what
    # makes the evidence exist.
    cost_totals: list[int] = []
    if to_evaluate:
        # Stratified, not uniform: balanced aggregation is useless if all of a
        # candidate's sampled tasks come from one class, which is what uniform
        # sampling of k=3 from an imbalanced rotation does most of the time.
        from harness.scorer import stratified_sample

        sampled = stratified_sample(adapter, rotation, max(1, tasks_per_candidate), rng)
        flat = pool.evaluate_many(
            adapter,
            [cand_dir for _, _, cand_dir, _, _, _, _, _ in to_evaluate for _ in sampled],
            [task for _ in to_evaluate for task in sampled],
        )
        fitnesses = []
        for i in range(len(to_evaluate)):
            per_task = flat[i * len(sampled) : (i + 1) * len(sampled)]
            aggregate, cost_total = _aggregate_fitness(per_task, sampled, adapter)
            fitnesses.append(aggregate)
            cost_totals.append(cost_total)
    else:
        fitnesses = []

    for (island_id, parent, cand_dir, cand, tokens, injected, proposal, arm), fitness, cost_total in zip(
        to_evaluate, fitnesses, cost_totals
    ):
        n_scored += 1
        parent_block = parent.get("block", seed_block)
        parent_root = _root_sha_for(parent, cand)
        n = _next_n(writer)
        writer.record(
            n,
            "scored",
            parent_sha=sha(parent_block),
            candidate_sha=sha(cand),
            candidate_block=cand,
            fitness=fitness,
            prompt_tokens=tokens,
            # Fitness.cost_tokens is the per-task mean, which is what keeps
            # scalar comparable; the row has to carry real spend, because
            # run_population sums this column for the token budget.
            cost_tokens_override=cost_total,
        )
        _set_generation_fields(conn, writer.solution_id, writer.run_id, n, generation, island_id, parent_root)
        _store_proposal(conn, writer, n, proposal)
        _set_arm(conn, writer, n, arm)
        completion_tokens_total += fitness.detail.get("completion_tokens", 0)

        # Before the validity gate below, on purpose: an invalid candidate is
        # a failure, and a lesson that was injected into one is exactly the
        # case retirement needs to hear about.
        _record_lesson_outcome(
            conn, writer.solution_id, writer.run_id, n, fitness, injected, vectorizer, categories
        )

        if not fitness.valid:
            continue
        iteration_id = _iteration_id_for_n(conn, writer.solution_id, writer.run_id, n)
        claimed = try_insert(conn, solution_id, island_id, fitness.descriptors, iteration_id, fitness.scalar)
        # The claim and the cell, on the row itself. Until 2026-10-16 neither
        # was stored: `elite` keeps only each cell's final occupant, so a
        # candidate that claimed a cell and was later displaced left no trace
        # outside the markdown generation report. PHASE-5.md task 5.1's
        # harvest filters on exactly this. `accepted` means "kept" in
        # hill-climb too, so it carries the same sense here.
        conn.execute(
            "update iteration set descriptors = %s, accepted = %s where id = %s",
            (list(fitness.descriptors), claimed, iteration_id),
        )
        conn.commit()
        if claimed:
            n_claimed += 1
            newly_claimed.append(
                {
                    "island_id": island_id,
                    "cell": fitness.descriptors,
                    "scalar": fitness.scalar,
                    "candidate_sha": sha(cand),
                    "parent_sha": sha(parent_block),
                }
            )

    # 4. migration (task 3.3)
    migration_log = []
    if should_migrate(generation):
        migration_log = migrate(conn, solution_id, n_islands)

    return GenerationResult(
        generation=generation,
        n_candidates=len(slots),
        n_parsed=n_parsed,
        n_admissible=n_admissible,
        n_scored=n_scored,
        n_claimed=n_claimed,
        completion_tokens=completion_tokens_total,
        migration_log=migration_log,
        newly_claimed=newly_claimed,
    )


def _next_n(writer: IterationWriter) -> int:
    with writer.conn.cursor() as cur:
        cur.execute(
            "select coalesce(max(n), -1) + 1 from iteration where solution_id = %s and run_id = %s",
            (writer.solution_id, writer.run_id),
        )
        return cur.fetchone()[0]


def _iteration_id_for_n(conn, solution_id: str, run_id, n: int) -> int:
    with conn.cursor() as cur:
        cur.execute(
            "select id from iteration where solution_id = %s and run_id = %s and n = %s",
            (solution_id, run_id, n),
        )
        return cur.fetchone()[0]


def _set_generation_fields(conn, solution_id: str, run_id, n: int, generation: int, island_id: int, root_sha: str) -> None:
    with conn.cursor() as cur:
        cur.execute(
            "update iteration set generation = %s, island_id = %s, root_sha = %s "
            "where solution_id = %s and run_id = %s and n = %s",
            (generation, island_id, root_sha, solution_id, run_id, n),
        )
    conn.commit()


def _expand_arms(all_parents: list, models: tuple[str, ...], rng: random.Random) -> list:
    """One proposal slot per parent per model, as
    (island_id, parent, inspirations, retrieved, model, pair_id).

    A single model is the ordinary generation, unchanged. With two, both arms
    get the same parent, inspirations and lessons, so their prompts are
    byte-identical and any difference within a pair is the proposer's. The
    arm order inside each pair is shuffled: both candidates enter the same
    archive, the first scored gets first claim on an empty cell, and a fixed
    order would bias the claim rate toward one arm."""
    slots = []
    for pair_id, (island_id, p, insp, retrieved) in enumerate(all_parents):
        order = list(models)
        if len(order) > 1:
            rng.shuffle(order)
        slots += [(island_id, p, insp, retrieved, m, pair_id) for m in order]
    return slots


def _model_label(model: str) -> str:
    """The proposer_model value for a LiteLLM role: the role itself, or for
    the distilled arm the role plus the adapter directory vLLM reports behind
    the "distilled" name.

    Raises if the distilled arm is requested while no adapter is loaded.
    Sending anyway would 404 and put LiteLLM's only proposer-distilled
    deployment into a cooldown that fails every request for the next five
    seconds (PHASE-5.md task 5.4), so the generation refuses to start."""
    if model != "proposer-distilled":
        return model
    import json
    import os
    from urllib.request import urlopen

    base = os.environ.get("VLLM_PROPOSER_URL", "http://localhost:8000")
    with urlopen(f"{base}/v1/models", timeout=10) as r:
        entries = json.load(r)["data"]
    root = next((m.get("root") for m in entries if m["id"] == "distilled"), None)
    if root is None:
        raise RuntimeError("proposer-distilled requested but no adapter is loaded as 'distilled' in vLLM")
    return f"{model}@{root}"


def _set_arm(conn, writer: IterationWriter, n: int, arm: tuple) -> None:
    """Which proposer produced row n, and which A/B pair it belongs to."""
    label, pair = arm
    conn.execute(
        "update iteration set proposer_model = %s, pair_id = %s where id = %s",
        (label, pair, _iteration_id_for_n(conn, writer.solution_id, writer.run_id, n)),
    )
    conn.commit()


def _store_proposal(conn, writer: IterationWriter, n: int, proposal: dict) -> None:
    """The proposer's context and response, on the row it produced.

    PHASE-5.md task 5.1 trains on context-to-proposal pairs, and until
    2026-10-16 the only copy of the context was Langfuse, which docs/backup.md
    deliberately does not back up. Postgres is backed up, so the pairs live
    here. Parse failures and inadmissible proposals are stored too: they are
    the negative half of any later preference pair (task 5.3)."""
    conn.execute(
        "update iteration set proposal = %s where id = %s",
        (Jsonb(proposal), _iteration_id_for_n(conn, writer.solution_id, writer.run_id, n)),
    )
    conn.commit()


def _fetch_block(candidate_sha: str | None) -> str | None:
    """Retrieves a past candidate's actual text from storage, keyed by
    its sha (harness.archive.cells() carries candidate_sha for exactly
    this). Without this, parent selection beyond generation 0 would
    silently degrade to the seed block instead of the real elite text —
    see the commit that added harness/storage.py for why."""
    if candidate_sha is None:
        return None
    from harness.storage import get_candidate

    return get_candidate(candidate_sha)
