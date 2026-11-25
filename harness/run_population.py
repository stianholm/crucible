"""Multi-generation population search driver. Ties together task 3.1-3.8.
See PHASE-3.md.
"""

from __future__ import annotations

import asyncio
import json
import statistics
import time
from importlib import import_module
from pathlib import Path

import yaml

from harness.archive import best_elite
from harness.budget import Budget
from harness.generation import run_generation
from harness.generation_report import generate_generation_report
from harness.halt import halted
from harness.events import record as record_event
from harness.held_out import eval_set_version, evaluate_against_held_out
from harness.incumbent import load_incumbent_block
from harness.islands import N_ISLANDS
from harness.lessons import retire_underperforming_significant
from harness.metrics import current_queue_depth, prefix_cache_hit_rate
from harness.persistence import IterationWriter, connect
from harness.sandbox_pool import SandboxPool, DEFAULT_SLOTS
from harness.storage import get_candidate
from harness.types import Task

REPO_ROOT = Path(__file__).resolve().parent.parent

# CAPACITY.yaml's own measured judge-profile knee_concurrency (Qwen3-4B,
# --gpu-memory-utilization 0.09) - distinct from the proposer's knee (32),
# and the real concurrency ceiling for judge-role calls on this hardware.
JUDGE_KNEE_CONCURRENCY = 16
# Held-out passes per end-of-run check. See the comment at the check itself.
HELD_OUT_PASSES = 2


def _load_adapter(solution_id: str):
    mod = import_module(f"solutions.{solution_id}.adapter")
    cls = next(v for k, v in vars(mod).items() if k.lower().endswith("adapter") and isinstance(v, type))
    return cls()


def _tasks_per_candidate(sol_dir: Path, override: int | None) -> int:
    """From the solution's own BASELINE.yaml, defaulting to 1 so a solution
    that has not opted in keeps the fitness its archive was measured under."""
    if override is not None:
        return override
    baseline = sol_dir / "BASELINE.yaml"
    if not baseline.exists():
        return 1
    doc = yaml.safe_load(baseline.read_text()) or {}
    return int((doc.get("feasibility") or {}).get("tasks_per_candidate") or 1)


def _load_rotation(sol_dir: Path) -> list[Task]:
    tasks = []
    for f in sorted((sol_dir / "data" / "rotation").glob("*.json")):
        d = json.loads(f.read_text())
        tasks.append(Task(task_id=d["task_id"], input=d["input"], expected=d.get("expected")))
    return tasks


async def _sample_queue_depth_during(coro, interval_s: float = 1.0):
    samples: list[int] = []
    stop = asyncio.Event()

    async def sampler():
        while not stop.is_set():
            d = current_queue_depth()
            if d is not None:
                samples.append(d)
            try:
                await asyncio.wait_for(stop.wait(), timeout=interval_s)
            except asyncio.TimeoutError:
                pass

    task = asyncio.create_task(sampler())
    try:
        result = await coro
    finally:
        stop.set()
        await task
    return result, samples


def run_population(
    solution_id: str,
    task_description: str | None = None,
    max_generations: int = 20,
    max_tokens: int = 10_000_000,
    max_wall_s: float = 8 * 3600,
    patience: int = 5,  # generations with zero new claims
    candidates_per_island: int = 16,
    n_islands: int = N_ISLANDS,
    grid_dims: tuple[int, int] = (6, 6),
    knee_concurrency: int = 32,
    sandbox_slots: int | None = None,
    temperature: float = 0.9,
    tasks_per_candidate: int | None = None,
    retire_lessons: bool = False,
    lessons: bool = False,
    proposer_models: tuple[str, ...] = ("proposer",),
    seed_block: str | None = None,
    report_dir: Path | None = None,
    report_tag: str = "",
) -> list[Path]:
    """tasks_per_candidate resolves from the solution's own BASELINE.yaml
    (`feasibility.tasks_per_candidate`), falling back to 1.

    One task per candidate turned out to be wrong twice over: candidates
    were ranked against each other on scores from different tasks, and a
    candidate that passed its single task produced no failure evidence,
    which starved task 4.3's retrieved lesson tier to nothing. See
    harness/generation.py's evaluation step.

    It is per solution rather than a global default because raising it is a
    fitness change in docs/change-procedures.md section 2's sense, which
    invalidates that solution's archive scores. A global default of 3 would
    have silently invalidated `fixture`'s baseline, and `fixture` is the
    harness's own regression test. AGENTS.md is also explicit that
    per-solution generation sizing lives in BASELINE.yaml, next to
    candidates_per_generation and sandbox_slots, which is what this is.

    retire_lessons=False reports retirement verdicts into each generation
    report without acting on them. The falsification loop has run for one
    generation as of 2026-09-29, and a store that retires a good lesson on a
    measurement artefact is worse than one that retires nothing, so acting is
    opt-in until the verdicts have been read against real accumulated data.

    lessons=False is PHASE-4.md task 4.5's arm A, the Phase 3 control. It
    passes sol_dir=None into run_generation, which is the same path a solution
    with no fitted taxonomy takes: no vectorizer load, no retrieval, no lesson
    blocks in the prompt, and no usage recorded. Everything else - the k=3
    evaluation, the archive, migration - is unchanged, so the arms differ in
    the one variable the ablation is about.

    **It is the default from 2026-09-30, because arm B lost.** At equal token
    budget, lesson memory scored held-out quality 0.3773 against the control's
    0.5227, on near-identical rotation scalars (0.8354 against 0.8319), while
    taking 33% more wall clock for two fewer generations. Equal on the set the
    search optimises against and much worse on the set it never sees is
    overfitting, and lessons are written from rotation failures, so the
    mechanism is available rather than mysterious.

    One run per arm is thin evidence, and the deficit is not established as
    causal - "best held-out candidate" is a maximum over hundreds of stochastic
    candidates whose run-to-run variance this project has never measured. But
    one measurement says worse and none says better, so on-by-default cannot be
    justified. See PHASE-4.md task 4.5 for what would reverse it."""
    sol_dir = REPO_ROOT / "solutions" / solution_id
    if task_description is None:
        # Question one plus the written standard from question eight (decision 80).
        from harness.onboarding import task_description as _task_description

        task_description = _task_description(sol_dir)
    tasks_per_candidate = _tasks_per_candidate(sol_dir, tasks_per_candidate)
    adapter = _load_adapter(solution_id)
    rotation = _load_rotation(sol_dir)
    # seed_block overrides the incumbent as the search's starting point without
    # replacing it (decision 85: restarting from an earlier lineage to escape
    # a local optimum the incumbent's descendants could not leave).
    seed_block = seed_block if seed_block is not None else load_incumbent_block(sol_dir)
    grid_size = grid_dims[0] * grid_dims[1]

    if sandbox_slots is None:
        # DEFAULT_SLOTS (8) is sized from real docker-container memory
        # headroom (decision 17) - irrelevant to a solution with no sandbox
        # at all. Reusing it here bottlenecked every capability_case
        # evaluation phase at 8-way concurrency regardless of how many
        # candidates a generation actually proposed, found 2026-09-24
        # investigating why a 64-candidate run wouldn't reveal anything
        # past a 32-candidate one. JUDGE_KNEE_CONCURRENCY below is
        # CAPACITY.yaml's own measured judge-profile knee (16, not the
        # proposer's 32) - the real concurrency ceiling for judge-role
        # calls on this hardware.
        sandbox_slots = DEFAULT_SLOTS if adapter.executes_code else JUDGE_KNEE_CONCURRENCY

    conn = connect()
    writer = IterationWriter(conn, solution_id)
    budget = Budget(max_iterations=max_generations, max_tokens=max_tokens, max_wall_s=max_wall_s, patience=patience)

    reports: list[Path] = []
    consecutive_empty = 0

    with SandboxPool(slots=sandbox_slots) as pool:
        for generation in budget.iterations():
            # PHASE-6.md's kill switch: a halt stops the run at the next
            # generation boundary, even one whose process the switch missed.
            if reason := halted():
                print(f"halted before generation {generation}: {reason}", flush=True)
                break
            gen_start = time.perf_counter()

            coro = run_generation(
                adapter=adapter,
                task_description=task_description,
                seed_block=seed_block,
                solution_id=solution_id,
                generation=generation,
                rotation=rotation,
                writer=writer,
                pool=pool,
                candidates_per_island=candidates_per_island,
                n_islands=n_islands,
                grid_dims=grid_dims,
                knee_concurrency=knee_concurrency,
                temperature=temperature,
                sol_dir=sol_dir if lessons else None,
                # Categorise failures even with lessons off, so task 4.5's
                # control arm still yields task 4.6's metrics.
                taxonomy_only_dir=sol_dir,
                tasks_per_candidate=tasks_per_candidate,
                proposer_models=proposer_models,
            )
            async def _generation_then_close(c=coro):
                from harness.proposal import close_async_client

                try:
                    return await _sample_queue_depth_during(c)
                finally:
                    await close_async_client()

            result, queue_samples = asyncio.run(_generation_then_close())

            # Token accounting for this generation: prompt_tokens (the
            # proposal call) plus cost_tokens (Fitness.cost_tokens - the
            # candidate's own invoke() call, plus a judge grading call where
            # needed). Summing prompt_tokens alone silently dropped every
            # evaluation-phase token, understating every past run's real
            # spend by roughly 60-95% for capability_case - found 2026-09-24
            # cross-checking a generation report's "tokens_used_total"
            # against Postgres directly. Also means max_tokens budgets were
            # never enforced against real spend until this fix.
            with conn.cursor() as cur:
                cur.execute(
                    "select coalesce(sum(prompt_tokens), 0) + coalesce(sum(cost_tokens), 0) "
                    "from iteration where solution_id = %s and run_id = %s and generation = %s",
                    (solution_id, writer.run_id, generation),
                )
                gen_tokens = cur.fetchone()[0]
            budget.spend_tokens(gen_tokens)

            budget_summary = {
                "generation": generation,
                "max_generations": budget.max_iterations,
                "tokens_used_total": budget.tokens_used,
                "max_tokens": budget.max_tokens,
                "elapsed_s_total": round(budget.elapsed_s, 1),
                "generation_wall_s": round(time.perf_counter() - gen_start, 1),
            }

            # Scheduled segments (harness/scheduler.py) write elsewhere under a
            # tag, so a day's segments do not overwrite each other's reports.
            report_path = (report_dir or sol_dir / "results") / f"GENERATION-{generation:03d}{'-' + report_tag if report_tag else ''}.md"
            report_path.parent.mkdir(parents=True, exist_ok=True)
            generate_generation_report(
                conn=conn,
                solution_id=solution_id,
                result=result,
                budget_summary=budget_summary,
                prefix_cache_hit_rate=prefix_cache_hit_rate(),
                queue_depth_samples=queue_samples,
                grid_size=grid_size,
                n_islands=n_islands,
                out_path=report_path,
            )
            reports.append(report_path)

            # PHASE-5.md task 5.4: per-arm and paired results, for this
            # generation and cumulatively, so a reader sees both the noise of
            # one generation and where the run is heading.
            if len(proposer_models) > 1:
                from harness.ab import render

                with report_path.open("a") as f:
                    f.write("\n" + render(conn, writer.run_id, generation))
                    f.write("\n" + render(conn, writer.run_id))
                from harness.diversity import render as render_diversity

                with report_path.open("a") as f:
                    f.write("\n" + render_diversity(conn, writer.run_id))

            # Lesson retirement (PHASE-4.md task 4.2's falsification loop),
            # appended to the generation report rather than run silently: a
            # retirement nobody can read the reasoning for is one nobody will
            # trust, and the verdicts for surviving lessons are as informative
            # as the retirements.
            #
            # dry_run until retire_lessons is set True by the caller. The whole
            # machinery has run for exactly one generation as of 2026-09-29, and
            # a store that retires a good lesson on a measurement artefact is
            # worse than one that retires nothing, so the default reports and
            # does not act.
            verdicts = retire_underperforming_significant(
                conn, solution_id, generation, dry_run=not retire_lessons
            )
            if verdicts:
                with report_path.open("a") as f:
                    f.write("\n## Lesson retirement" + ("" if retire_lessons else " (dry run)") + "\n\n")
                    for lesson_id, retired, reason in verdicts:
                        mark = "RETIRED" if retired else "kept"
                        f.write(f"- Lesson {lesson_id}: **{mark}** — {reason}\n")

            consecutive_empty = 0 if result.n_claimed > 0 else consecutive_empty + 1
            if consecutive_empty >= patience:
                break

    # Self-grading coupling (BASELINE.yaml) is watched for here, not just
    # disclosed: a best-ever candidate that scores well on rotation without a
    # matching held-out improvement is what exploiting that coupling looks
    # like, so check the archive's actual best-ever candidate against
    # held-out once, at the end of the run, the same way run.py does for
    # hill-climb.
    best = max(
        (e for e in (best_elite(conn, solution_id, isl) for isl in range(n_islands)) if e),
        key=lambda e: e["scalar"],
        default=None,
    )
    # Close the read transaction before the held-out check: it takes up to 40
    # minutes, and an idle open transaction that long blocks vacuum (the
    # same reason as generation.py's commit before the proposal fan-out).
    conn.commit()
    if best is not None and reports and not halted():
        best_block = get_candidate(best["candidate_sha"])
        if best_block is not None:
            # Scored twice, not once: re-scoring one capability_case candidate
            # moved its held-out quality by 0.158 (TODO.md decision 64), so a
            # single pass is a noisy sample rather than a measurement. Both
            # passes are reported so the spread is visible next to the mean.
            passes = [evaluate_against_held_out(adapter, sol_dir, best_block) for _ in range(HELD_OUT_PASSES)]
            with reports[-1].open("a") as f:
                f.write("\n## Held-out check (best-ever candidate)\n\n")
                f.write(f"- Candidate: `{best['candidate_sha']}` (rotation scalar {best['scalar']:.4f})\n")
                f.write(f"- Held-out quality: {statistics.mean(p.quality for p in passes):.4f}"
                        f" (passes: {', '.join(f'{p.quality:.4f}' for p in passes)})\n")
                f.write(f"- Held-out scalar: {statistics.mean(p.scalar for p in passes):.4f}"
                        f" (passes: {', '.join(f'{p.scalar:.4f}' for p in passes)})\n")
                f.write(f"- All held-out tasks valid: {all(p.all_valid for p in passes)}\n")
            record_event(
                conn, "held_out", solution_id,
                run_id=str(writer.run_id), candidate_sha=best["candidate_sha"],
                rotation_scalar=float(best["scalar"]),
                quality=statistics.mean(p.quality for p in passes),
                passes=[p.quality for p in passes],
                all_valid=all(p.all_valid for p in passes),
                eval_version=eval_set_version(sol_dir),
                # Generations in which anything was scored. A generation whose
                # proposals all failed (proposer down) tested nothing, and
                # counting it would let an outage climb the plateau ladder.
                generations=conn.execute(
                    "select count(distinct generation) from iteration "
                    "where run_id = %s and status = 'scored'", (writer.run_id,)).fetchone()[0],
                generations_run=len(reports),
                temperature=temperature,
            )

    conn.close()
    return reports
