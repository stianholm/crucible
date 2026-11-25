"""Generates capability_case_author's task set. See PHASE-1.md task 1.1.

Scenarios come from capability_case's generator (same seed, same mechanical
floor), reframed as the requesting team's raw notes rather than a submitted
case. Task ids are prefixed `author-`, so harness/split.py's hash assigns them
to splits independently of capability_case's: sealing one solution's held-out
set says nothing about the other's.

Usage: python -m solutions.capability_case_author.checks.generate_tasks
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from harness.split import split_of
from solutions.capability_case.checks.generate_tasks import build_scenarios
from solutions.capability_case.checks.rubric import mechanical_floor
from solutions.capability_case_author.checks.rubric import reason_keys

SOL_DIR = Path(__file__).resolve().parent.parent


def notes_for(scenario) -> str:
    """capability_case's narrative, reframed: the first paragraph says what the
    team wants, the rest are its evidence and plan notes, unchanged."""
    paras = scenario.narrative.split("\n\n")
    head = (f"Notes from an operations team that wants to {scenario.requested_relaxation} without "
            "per-action human approval, through the operational change gateway. Write their capability case.")
    return "\n\n".join([head] + [f"- {p}" for p in paras[1:]])


def build_tasks() -> list[dict]:
    tasks = []
    for s in build_scenarios():
        floor = mechanical_floor(s)
        tid = f"author-{s.proposal_id}"
        tasks.append({
            "task_id": tid,
            "input": json.dumps({"scenario_id": tid, "notes": notes_for(s)}),
            "expected": {
                "must_reject": floor.must_reject,
                "reasons": floor.reasons,
                "reason_keys": reason_keys(floor.reasons),
                # Ground truth here, unlike capability_case: the strength-honesty
                # check grades each dimension's stated strength against it.
                "evidence": s.evidence,
            },
        })
    return tasks


def main() -> None:
    tasks = build_tasks()
    by_split: dict[str, list[dict]] = {"dev": [], "rotation": [], "held_out": []}
    for t in tasks:
        by_split[split_of(t["task_id"])].append(t)
    for split, items in by_split.items():
        d = SOL_DIR / "data" / split
        d.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.json"):
            f.unlink()
        for item in items:
            (d / f"{item['task_id']}.json").write_text(json.dumps(item, indent=2))
    # Seal held-out: a checksum over its sorted contents, as capability_case does.
    h = hashlib.sha256()
    for f in sorted((SOL_DIR / "data" / "held_out").glob("*.json")):
        h.update(f.read_bytes())
    (SOL_DIR / "data" / "held_out.sha256").write_text(f"{h.hexdigest()}  -\n")
    rej = {s: sum(t["expected"]["must_reject"] for t in v) for s, v in by_split.items()}
    print({s: f"{len(v)} ({rej[s]} must-reject)" for s, v in by_split.items()})


if __name__ == "__main__":
    main()
