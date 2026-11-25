"""Adversarial suite for the scorer. See PHASE-1.md task 1.6.

Each candidate here is a hand-crafted attack on the fixture's fitness
function. The framing in PHASE-1.md's table assumes an LLM-agent-shaped
solution (empty completion, refusal, etc.); the fixture is deterministic
Python dispatch code, so each attack is translated to what it actually
means for this shape — the intent (gates work, cost/latency are penalised,
the split doesn't leak) is what's being tested, not the literal wording.
"""

from __future__ import annotations

import json
import statistics
import textwrap
from pathlib import Path

import pytest

from harness.scorer import MAX_WALL_S, evaluate
from harness.types import Task
from solutions.fixture.adapter import FixtureAdapter

SOL_DIR = Path(__file__).resolve().parent.parent / "solutions" / "fixture"


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
def adapter() -> FixtureAdapter:
    return FixtureAdapter()


@pytest.fixture(scope="module")
def rotation() -> list[Task]:
    return _load_split("rotation")


@pytest.fixture(scope="module")
def dev() -> list[Task]:
    return _load_split("dev")


@pytest.fixture(scope="module")
def one_rotation_task(rotation) -> Task:
    return rotation[0]


def _mean_quality(adapter: FixtureAdapter, cand_dir: Path, tasks: list[Task]) -> float:
    return statistics.mean(evaluate(adapter, cand_dir, t).quality for t in tasks)


def test_returns_nothing_scores_zero(adapter, one_rotation_task):
    block = "return None"
    cand_dir = adapter.materialise(block)
    f = evaluate(adapter, cand_dir, one_rotation_task)
    assert f.quality == 0.0


def test_echoes_input_verbatim_scores_near_zero(adapter, rotation):
    cand_dir = adapter.materialise("return req")
    mean_q = _mean_quality(adapter, cand_dir, rotation)
    assert mean_q < 0.05, f"echoing the input should not accidentally match expected outputs, got {mean_q}"


def test_raises_immediately_is_invalid_with_error_captured(adapter, one_rotation_task):
    block = 'raise RuntimeError("boom")'
    cand_dir = adapter.materialise(block)
    f = evaluate(adapter, cand_dir, one_rotation_task)
    assert f.valid is False
    assert f.quality == 0.0
    assert "boom" in f.detail["raw"]["stderr"]
    # confirm no downstream tokens/cost were charged for a candidate that never produced output
    assert f.cost_tokens == 0


def test_sleeps_past_wall_clock_recovers(adapter, one_rotation_task):
    block = f"import time as _t; _t.sleep({MAX_WALL_S + 5}); return None"
    cand_dir = adapter.materialise(block)
    f = evaluate(adapter, cand_dir, one_rotation_task)
    assert f.valid is False
    assert f.quality == 0.0
    # the harness must recover within roughly the timeout, not hang
    assert f.latency_s <= MAX_WALL_S + 2.0


def test_correct_but_much_slower_is_penalised_on_scalar(adapter, one_rotation_task):
    fast_block = _incumbent_block()
    # graft a 3s sleep onto the otherwise-correct incumbent logic, so
    # quality stays 1.0 but latency balloons. dedent fast_block to a
    # consistent 0-baseline first — materialise() re-indents the whole
    # combined block uniformly, so mixing an already-indented block with a
    # fresh top-level line here would double up its indentation.
    slow_block = "import time as _t; _t.sleep(3.0)\n" + textwrap.dedent(fast_block)

    fast_dir = adapter.materialise(fast_block)
    slow_dir = adapter.materialise(slow_block)

    f_fast = evaluate(adapter, fast_dir, one_rotation_task)
    f_slow = evaluate(adapter, slow_dir, one_rotation_task)

    assert f_slow.quality == f_fast.quality  # correctness unaffected
    assert f_slow.latency_s > f_fast.latency_s + 2.5
    assert f_slow.scalar < f_fast.scalar  # cost/latency penalty visible in the scalar


def test_hardcoding_dev_does_not_generalise_to_rotation(adapter, dev, rotation):
    # dev's one task is factorial(0) -> 1. Hardcode exactly that, fail
    # everything else outright.
    dev_task = dev[0]
    dev_args = json.loads(dev_task.input)["args"]
    # relative indentation matters here: materialise() re-indents the whole
    # block uniformly, so `return` must be one level deeper than `if`, and
    # `raise` (the fallback) back at `if`'s own level.
    block = (
        f'if op == "factorial" and args == {dev_args}:\n'
        f"    return {dev_task.expected}\n"
        f'raise RuntimeError("not implemented")'
    )
    cand_dir = adapter.materialise(block)

    dev_score = _mean_quality(adapter, cand_dir, dev)
    rotation_score = _mean_quality(adapter, cand_dir, rotation)

    assert dev_score == 1.0
    assert rotation_score < 0.05, (
        "a candidate that hardcodes the dev answer scored well on rotation too — "
        "the splits are leaking information"
    )


def test_incumbent_unchanged_matches_baseline_exactly(adapter, rotation):
    # the fixture's scorer is fully deterministic (no judge, no sampling),
    # so noise_sigma is 0 and repeat runs must match exactly, not just
    # "within one sigma".
    block = _incumbent_block()
    cand_dir = adapter.materialise(block)
    mean_q = _mean_quality(adapter, cand_dir, rotation)
    assert mean_q == pytest.approx(25 / 31, abs=1e-9)  # measured baseline, see BASELINE.yaml
