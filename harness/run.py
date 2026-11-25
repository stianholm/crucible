"""Ties task 2.1-2.7 together into one runnable hill-climb. See PHASE-2.md."""

from __future__ import annotations

import json
from importlib import import_module
from pathlib import Path

import yaml

from harness.budget import Budget
from harness.held_out import evaluate_against_held_out
from harness.incumbent import load_incumbent_block
from harness.loop import hill_climb
from harness.persistence import IterationWriter, connect
from harness.report import generate_run_report
from harness.types import Task

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_adapter(solution_id: str):
    mod = import_module(f"solutions.{solution_id}.adapter")
    cls = next(v for k, v in vars(mod).items() if k.lower().endswith("adapter") and isinstance(v, type))
    return cls()


def _load_rotation(sol_dir: Path) -> list[Task]:
    tasks = []
    for f in sorted((sol_dir / "data" / "rotation").glob("*.json")):
        d = json.loads(f.read_text())
        tasks.append(Task(task_id=d["task_id"], input=d["input"], expected=d.get("expected")))
    return tasks


def run(
    solution_id: str,
    task_description: str,
    max_iterations: int = 50,
    max_tokens: int = 2_000_000,
    max_wall_s: float = 4 * 3600,
    patience: int = 12,
    temperature: float = 0.9,
) -> Path:
    sol_dir = REPO_ROOT / "solutions" / solution_id
    baseline = yaml.safe_load((sol_dir / "BASELINE.yaml").read_text())

    adapter = _load_adapter(solution_id)
    rotation = _load_rotation(sol_dir)
    incumbent_block = load_incumbent_block(sol_dir)

    conn = connect()
    writer = IterationWriter(conn, solution_id)
    budget = Budget(
        max_iterations=max_iterations,
        max_tokens=max_tokens,
        max_wall_s=max_wall_s,
        patience=patience,
    )

    final_block = hill_climb(
        adapter=adapter,
        task_description=task_description,
        incumbent_block=incumbent_block,
        rotation=rotation,
        baseline_scalar=baseline["baseline"]["scalar_mean"],
        baseline_sigma=baseline["baseline"]["noise_sigma"],
        writer=writer,
        budget=budget,
        temperature=temperature,
    )

    held_out_score = evaluate_against_held_out(adapter, sol_dir, final_block)

    rows = writer.fetch_run()
    budget_summary = {
        "max_iterations": budget.max_iterations,
        "max_tokens": budget.max_tokens,
        "max_wall_s": budget.max_wall_s,
        "patience": budget.patience,
        "actual_iterations": budget.iteration_count,
        "actual_tokens": budget.tokens_used,
        "actual_wall_s": round(budget.elapsed_s, 1),
        "stop_reason": budget.exhaustion_reason() or "patience exhausted",
    }
    run_md = sol_dir / "RUN.md"
    generate_run_report(
        rows=rows,
        solution_id=solution_id,
        run_id=str(writer.run_id),
        budget_summary=budget_summary,
        baseline_scalar=baseline["baseline"]["scalar_mean"],
        out_path=run_md,
        held_out=held_out_score,
    )

    conn.close()
    return run_md
