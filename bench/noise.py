"""Measure the noise floor of a solution's scorer over its rotation set.
See PHASE-1.md task 1.5. Any improvement smaller than roughly twice
noise_sigma is not distinguishable from randomness.

Usage: python -m bench.noise <solution_id> [--candidate-sha SHA]

Without --candidate-sha, measures the solution's current incumbent (the
original use case: BASELINE.yaml's baseline noise floor). With it, measures
an arbitrary evolved candidate pulled from storage instead — added for
capability_case's evolved, reasoning-loop-risk-bearing candidates, whose
noise floor was never measured because BASELINE.yaml's noise_sigma: 0.0 was
taken against the simpler original incumbent, before that failure mode was
known. See PHASE-3.md task 3.9's third run.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from importlib import import_module
from pathlib import Path

from harness.incumbent import load_incumbent_block
from harness.scorer import evaluate
from harness.storage import get_candidate
from harness.types import Task

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_rotation(sol_dir: Path) -> list[Task]:
    tasks = []
    for f in sorted((sol_dir / "data" / "rotation").glob("*.json")):
        d = json.loads(f.read_text())
        tasks.append(Task(task_id=d["task_id"], input=d["input"], expected=d.get("expected")))
    return tasks


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("solution_id")
    p.add_argument("--runs", type=int, default=7)
    p.add_argument("--candidate-sha", default=None, help="measure this stored candidate instead of the incumbent")
    args = p.parse_args(argv)

    sol_dir = REPO_ROOT / "solutions" / args.solution_id
    adapter_mod = import_module(f"solutions.{args.solution_id}.adapter")
    adapter_cls = next(
        v for k, v in vars(adapter_mod).items() if k.lower().endswith("adapter") and isinstance(v, type)
    )
    adapter = adapter_cls()

    if args.candidate_sha:
        block = get_candidate(args.candidate_sha)
        if block is None:
            print(f"no stored candidate found for sha {args.candidate_sha!r}", file=sys.stderr)
            return 1
    else:
        block = load_incumbent_block(sol_dir)
    rotation = load_rotation(sol_dir)

    runs = []
    for _ in range(args.runs):
        cand_dir = adapter.materialise(block)
        scores = [evaluate(adapter, cand_dir, t).quality for t in rotation]
        runs.append(statistics.mean(scores))

    sigma = statistics.stdev(runs) if len(runs) > 1 else 0.0
    mean = statistics.mean(runs)
    print(f"runs: {runs}")
    print(f"suite mean {mean:.6f}  sigma {sigma:.6f}")
    print(f"significance threshold for phase 2: {2 * sigma:.6f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
