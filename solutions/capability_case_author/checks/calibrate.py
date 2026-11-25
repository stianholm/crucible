"""Judge calibration for capability_case_author (PHASE-1.md's judge discipline).

The judge only grades argument quality on floor-passing scenarios, but that is
30% of quality there, and capability_case's judge needed two rubric revisions
against hand-graded labels before it could be trusted. Same procedure here:

    python -m solutions.capability_case_author.checks.calibrate sheet     # writes the sheet + label file
    # a person reads the sheet and fills in calibration_labels.yaml
    python -m solutions.capability_case_author.checks.calibrate score     # judge vs human agreement

Items mix two instructions, the naive "persuasive" seed and an honest
hand-written reference, so the human grades span the scale rather than
clustering at one band. Neither instruction is shown to the grader.
"""

from __future__ import annotations

import json
import random
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

SOL = Path(__file__).resolve().parent.parent
SHEET = SOL / "calibration_sheet.md"
LABELS = SOL / "calibration_labels.yaml"
ITEMS = SOL / "calibration_items.json"

HONEST = """You write capability cases for a review board that will check every claim.
State only what the team's notes say; never add a figure, a test or a control that
is not in them. For each evidence dimension, say plainly what the notes show and
how strong it is: a short informal list is thin, a self-review is not an audit.
Call thin evidence thin and say what would close the gap. If the notes show a
disqualifier under Section 8/9, name it and recommend not proceeding; otherwise
the disqualifiers section is "None", and thin evidence means gathering more
evidence, not rejection. Be specific and brief."""


def _floor_pass_tasks():
    from harness.types import Task

    out = []
    for split in ("dev", "rotation"):
        for f in sorted((SOL / "data" / split).glob("*.json")):
            d = json.loads(f.read_text())
            if not d["expected"]["must_reject"]:
                out.append(Task(task_id=d["task_id"], input=d["input"], expected=d["expected"]))
    return out


def sheet(n: int = 24, seed: int = 20261019) -> None:
    from harness.incumbent import load_incumbent_block
    from harness.run_population import _load_adapter
    from solutions.capability_case_author.checks.rubric import sections

    a = _load_adapter("capability_case_author")
    rng = random.Random(seed)
    tasks = rng.sample(_floor_pass_tasks(), n // 2)
    cands = {"seed": a.materialise(load_incumbent_block(SOL)), "honest": a.materialise(HONEST)}
    jobs = [(t, which) for t in tasks for which in cands]
    rng.shuffle(jobs)

    def run(job):
        t, which = job
        return t, which, a.judge_view(a.invoke(cands[which], t.input, 900).output or "")

    with ThreadPoolExecutor(16) as ex:
        done = list(ex.map(run, jobs))
    items = []
    lines = ["# capability_case_author judge calibration", "",
             "Grade each case's argument quality 0-3 using the rubric below, in "
             "`calibration_labels.yaml`. Structure, strength labels, the recommendation and "
             "invented numbers are checked mechanically; grade the argument only.", "",
             "```", __import__("solutions.capability_case_author.checks.rubric", fromlist=["x"]).JUDGE_RUBRIC, "```", ""]
    for i, (t, which, case) in enumerate(done, 1):
        item_id = f"c{i:02d}"
        items.append({"id": item_id, "task_id": t.task_id, "instruction": which, "case": case,
                      "input": t.input})
        lines += [f"## {item_id}", "", "**Notes**", "", json.loads(t.input)["notes"], "", "**Case**", "", case, "", "---", ""]
    ITEMS.write_text(json.dumps(items, indent=1))
    SHEET.write_text("\n".join(lines))
    LABELS.write_text("# BAND 0-3 per item, from calibration_sheet.md. Leave a comment if unsure.\n"
                      + "".join(f"{it['id']}: \n" for it in items))
    print(f"wrote {SHEET} and {LABELS} ({len(items)} items)")


def score() -> None:
    from harness.judge import score_with_judge
    from solutions.capability_case_author.checks.rubric import JUDGE_RUBRIC

    items = {it["id"]: it for it in json.loads(ITEMS.read_text())}
    labels = {k: int(v) for k, v in (yaml.safe_load(LABELS.read_text()) or {}).items() if v not in (None, "")}
    missing = sorted(set(items) - set(labels))
    if missing:
        raise SystemExit(f"unlabelled items: {missing}")

    def judge(it):
        s, *_ = score_with_judge(JUDGE_RUBRIC, f"## Task\n{it['input']}\n\n## Candidate's response\n{it['case']}")
        return it["id"], round(s * 3)

    with ThreadPoolExecutor(16) as ex:
        bands = dict(ex.map(judge, items.values()))
    exact = sum(bands[k] == labels[k] for k in labels)
    within = sum(abs(bands[k] - labels[k]) <= 1 for k in labels)
    print(f"exact {exact}/{len(labels)}, within one band {within}/{len(labels)}")
    for k in sorted(labels):
        if bands[k] != labels[k]:
            print(f"  {k} ({items[k]['instruction']}): human {labels[k]}, judge {bands[k]}")


if __name__ == "__main__":
    {"sheet": sheet, "score": score}[sys.argv[1]]()
