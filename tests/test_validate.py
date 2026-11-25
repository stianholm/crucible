"""See PHASE-2.md task 2.2 verify: each rejection reason fires at least
once against a hand-written bad candidate."""

from __future__ import annotations

from pathlib import Path

import pytest

from harness.validate import admissible
from solutions.fixture.adapter import FixtureAdapter

SOL_DIR = Path(__file__).resolve().parent.parent / "solutions" / "fixture"


@pytest.fixture()
def adapter() -> FixtureAdapter:
    return FixtureAdapter()


@pytest.fixture()
def parent_block() -> str:
    text = (SOL_DIR / "candidate" / "candidate.py").read_text()
    return text.split("# EVOLVE-BLOCK-START")[1].split("# EVOLVE-BLOCK-END")[0].strip("\n")


def test_unchanged_is_rejected(adapter, parent_block):
    ok, why = admissible(parent_block, parent_block, adapter.materialise)
    assert not ok
    assert why == "unchanged"


def test_excessive_growth_is_rejected(adapter, parent_block):
    bloated = parent_block + "\n" + "x = 1\n" * (len(parent_block) * 4)
    ok, why = admissible(bloated, parent_block, adapter.materialise)
    assert not ok
    assert why.startswith("grew")


def test_syntax_error_is_rejected(adapter, parent_block):
    ok, why = admissible("if op == :\n    pass", parent_block, adapter.materialise)
    assert not ok
    assert why.startswith("syntax:")


def test_signature_change_is_rejected(adapter, parent_block):
    # redefines the frozen solve() entrypoint instead of just filling the body
    block = (
        "return None\n"
        "\n"
        "def solve(task_input, ctx=None):\n"
        "    return '{}'"
    )
    ok, why = admissible(block, parent_block, adapter.materialise)
    assert not ok
    assert why == "signature changed"


def test_reaches_evaluator_is_rejected(adapter, parent_block):
    block = "import harness.scorer\nreturn None"
    ok, why = admissible(block, parent_block, adapter.materialise)
    assert not ok
    assert why == "imports the evaluator"


def test_good_candidate_is_admissible(adapter, parent_block):
    tweaked = parent_block.replace('elif op == "gcd":', 'elif op == "gcd":  # tweaked')
    ok, why = admissible(tweaked, parent_block, adapter.materialise)
    assert ok
    assert why == "ok"
