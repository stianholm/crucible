"""Adversarial suite for itot_classifier. See PHASE-1.md task 1.6.

Same attacks as tests/test_fitness.py, translated to this solution's
shape: output is a structured multi-field classification (gateway,
approved, anti_patterns_detected) graded with partial credit per field,
not a single scalar graded pass/fail — so a few assertions (the "echo"
and "hardcode" attacks) land differently here than in the fixture, and
that difference is itself worth documenting inline rather than silently
copying the fixture's thresholds.
"""

from __future__ import annotations

import json
import statistics
import textwrap
from pathlib import Path

import pytest

from harness.scorer import MAX_WALL_S, evaluate
from harness.types import Task
from solutions.itot_classifier.adapter import ItotClassifierAdapter

SOL_DIR = Path(__file__).resolve().parent.parent / "solutions" / "itot_classifier"


def _load_split(name: str) -> list[Task]:
    tasks = []
    for f in sorted((SOL_DIR / "data" / name).glob("*.json")):
        d = json.loads(f.read_text())
        tasks.append(Task(task_id=d["task_id"], input=d["input"], expected=d["expected"]))
    return tasks


def _incumbent_block() -> str:
    text = (SOL_DIR / "candidate" / "candidate.py").read_text()
    return text.split("# EVOLVE-BLOCK-START")[1].split("# EVOLVE-BLOCK-END")[0].strip("\n")


@pytest.fixture(scope="module")
def adapter() -> ItotClassifierAdapter:
    return ItotClassifierAdapter()


@pytest.fixture(scope="module")
def rotation() -> list[Task]:
    return _load_split("rotation")


@pytest.fixture(scope="module")
def dev() -> list[Task]:
    return _load_split("dev")


@pytest.fixture(scope="module")
def one_rotation_task(rotation) -> Task:
    return rotation[0]


def _mean_quality(adapter: ItotClassifierAdapter, cand_dir: Path, tasks: list[Task]) -> float:
    return statistics.mean(evaluate(adapter, cand_dir, t).quality for t in tasks)


def test_returns_nothing_scores_zero(adapter, one_rotation_task):
    block = "return None"
    cand_dir = adapter.materialise(block)
    f = evaluate(adapter, cand_dir, one_rotation_task)
    assert f.quality == 0.0


def test_echoes_input_verbatim_gates_to_zero(adapter, rotation):
    # echoing the proposal back has no "gateway" key at all, so this fails
    # shape_ok outright (gate, not a programmatic-check partial score) —
    # unlike the fixture, where echoing produces valid-shaped-but-wrong
    # output and lands in the programmatic tier instead.
    cand_dir = adapter.materialise("return p")
    mean_q = _mean_quality(adapter, cand_dir, rotation)
    assert mean_q == 0.0, "echoing the input has no 'gateway' key and must fail the shape gate, not partially score"


def test_raises_immediately_is_invalid_with_error_captured(adapter, one_rotation_task):
    block = 'raise RuntimeError("boom")'
    cand_dir = adapter.materialise(block)
    f = evaluate(adapter, cand_dir, one_rotation_task)
    assert f.valid is False
    assert f.quality == 0.0
    assert "boom" in f.detail["raw"]["stderr"]
    assert f.cost_tokens == 0


def test_sleeps_past_wall_clock_recovers(adapter, one_rotation_task):
    block = f"import time as _t; _t.sleep({MAX_WALL_S + 5}); return None"
    cand_dir = adapter.materialise(block)
    f = evaluate(adapter, cand_dir, one_rotation_task)
    assert f.valid is False
    assert f.quality == 0.0
    assert f.latency_s <= MAX_WALL_S + 2.0


def test_correct_but_much_slower_is_penalised_on_scalar(adapter, one_rotation_task):
    fast_block = _incumbent_block()
    slow_block = "import time as _t; _t.sleep(3.0)\n" + textwrap.dedent(fast_block)

    fast_dir = adapter.materialise(fast_block)
    slow_dir = adapter.materialise(slow_block)

    f_fast = evaluate(adapter, fast_dir, one_rotation_task)
    f_slow = evaluate(adapter, slow_dir, one_rotation_task)

    assert f_slow.quality == f_fast.quality
    assert f_slow.latency_s > f_fast.latency_s + 2.5
    assert f_slow.scalar < f_fast.scalar


def test_hardcoding_dev_does_not_generalise_to_rotation(adapter, dev, rotation):
    # dev's clean-01 -> {gateway: telemetry, approved: true, anti_patterns: []}.
    # Hardcode exactly that one proposal_id, answer something plausible-but-
    # wrong for everything else.
    dev_task = next(t for t in dev if json.loads(t.input)["proposal_id"] == "clean-01")
    block = (
        'if p.get("proposal_id") == "clean-01":\n'
        '    return {"gateway": "telemetry", "approved": True, "required_controls": [], '
        '"anti_patterns_detected": [], "reasoning": "hardcoded"}\n'
        'return {"gateway": "operational_change", "approved": False, "required_controls": [], '
        '"anti_patterns_detected": ["shared_identity"], "reasoning": "wrong on purpose"}'
    )
    cand_dir = adapter.materialise(block)

    dev_score = _mean_quality(adapter, cand_dir, dev)
    rotation_score = _mean_quality(adapter, cand_dir, rotation)

    assert dev_score >= 1.0 / len(dev)  # the hardcoded task itself scores perfectly
    dev_task_fitness = evaluate(adapter, cand_dir, dev_task)
    assert dev_task_fitness.quality == 1.0
    # this solution grades three fields with partial (Jaccard) credit on
    # anti-patterns rather than the fixture's binary per-task pass/fail, so
    # an always-wrong fallback still picks up some accidental anti-pattern
    # overlap on rotation tasks whose expected set happens to include
    # "shared_identity", or is empty. 0.25 is well below the measured
    # incumbent's 0.862 rotation quality and is not achievable by chance
    # gateway/approved matching alone (both wrong on every non-hardcoded
    # task here) — real headroom is not leaking from dev into rotation.
    assert rotation_score < 0.25, (
        "a candidate that hardcodes the dev answer scored too well on rotation — "
        "the splits may be leaking information"
    )


def test_incumbent_unchanged_matches_baseline_exactly(adapter, rotation):
    # deterministic scorer (no judge, no sampling): noise_sigma is 0, so
    # repeat runs must match the measured baseline exactly. The incumbent
    # is the hill-climb winner promoted after RUN.md's search (see
    # BASELINE.yaml) — quality_mean is the ceiling, 1.0, not the original
    # onboarding baseline's 0.862.
    block = _incumbent_block()
    cand_dir = adapter.materialise(block)
    mean_q = _mean_quality(adapter, cand_dir, rotation)
    assert mean_q == pytest.approx(1.0, abs=1e-9)  # measured baseline, see BASELINE.yaml


def test_partial_credit_on_anti_patterns_is_real(adapter, rotation):
    # a candidate that gets gateway+approved right on every task but never
    # detects any anti-pattern should score strictly between 0 and 1 on
    # rotation as a whole (not collapse to a binary pass/fail the way the
    # fixture's exact-match design does) — proving the Jaccard partial-
    # credit path in programmatic_checks() actually reaches the scorer.
    #
    # Written as a fixed, self-contained block rather than a surgical edit
    # of _incumbent_block()'s literal source: the incumbent is not frozen
    # the way the fixture's is (it's expected to change as real
    # improvements land — this file already promoted a hill-climb winner
    # once), and a regex/string-surgery test that assumes a specific
    # incumbent syntax breaks silently the next time it does.
    block = (
        'if p.get("touches_sis"):\n'
        '    gateway = "safety_wall"\n'
        '    approved = False\n'
        'elif p.get("needs_write"):\n'
        '    gateway = "operational_change"\n'
        '    approved = bool(p.get("within_approved_scope"))\n'
        "else:\n"
        '    data_type = p.get("data_type")\n'
        '    gateway = "telemetry" if data_type == "live_process" else "engineering_data"\n'
        '    approved = bool(p.get("within_approved_scope"))\n'
        "return {\n"
        '    "gateway": gateway,\n'
        '    "approved": approved,\n'
        '    "anti_patterns_detected": [],\n'
        "}"
    )
    cand_dir = adapter.materialise(block)
    mean_q = _mean_quality(adapter, cand_dir, rotation)
    assert 0.0 < mean_q < 1.0
    assert mean_q != pytest.approx(1.0, abs=1e-9)  # must differ from the incumbent's own (ceiling) score
