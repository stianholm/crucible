"""Held-out evaluation, shared by hill-climb and population-search reporting.

Held-out is loaded and scored exactly like rotation (score_over is generic
over any task list) — the only reason this isn't just an inline call at each
site is that both harness/run.py and harness/run_population.py need it. Making
it a standing part of every run's report, rather than a one-off script run by
hand afterward, is what turns the self-grading-coupling risk documented in
solutions/capability_case/BASELINE.yaml from a sentence into an actual check:
a candidate scoring well on rotation without a matching held-out improvement
is what exploiting that coupling would look like.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from harness.adapter import SolutionAdapter
from harness.loop import AggregateScore, score_over
from harness.types import Task


def load_held_out(sol_dir: Path) -> list[Task]:
    tasks = []
    for f in sorted((sol_dir / "data" / "held_out").glob("*.json")):
        d = json.loads(f.read_text())
        tasks.append(Task(task_id=d["task_id"], input=d["input"], expected=d.get("expected")))
    return tasks


def eval_set_version(sol_dir: Path) -> str:
    """A short hash of the held-out set's files. PHASE-6.md: every recorded
    score is stamped with it, and the morning report refuses to compare
    scores across versions without saying so."""
    h = hashlib.sha256()
    for f in sorted((sol_dir / "data" / "held_out").glob("*.json")):
        h.update(f.name.encode() + b"\0" + f.read_bytes() + b"\0")
    return h.hexdigest()[:12]


def evaluate_against_held_out(adapter: SolutionAdapter, sol_dir: Path, candidate_block: str) -> AggregateScore:
    held_out = load_held_out(sol_dir)
    cand_dir = adapter.materialise(candidate_block)
    return score_over(adapter, cand_dir, held_out)
