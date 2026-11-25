"""The abuse suite. See PHASE-2.md task 2.3.

Run before every Phase 3 generation; treat a failure as a blocking bug. A
sandbox slot that leaks one container per run leaks sixty-four per
generation once Phase 3 scales this to a pool.
"""

from __future__ import annotations

import subprocess

import pytest

from harness.sandbox import run_in_sandbox
from solutions.fixture.adapter import FixtureAdapter


def _containers_matching(prefix: str) -> list[str]:
    out = subprocess.run(
        ["docker", "ps", "-a", "--filter", f"name={prefix}", "--format", "{{.Names}}"],
        capture_output=True,
        text=True,
    )
    return [line for line in out.stdout.splitlines() if line.strip()]


@pytest.fixture()
def adapter() -> FixtureAdapter:
    return FixtureAdapter()


def test_infinite_loop_is_killed_at_wall_clock(adapter):
    cand_dir = adapter.materialise("while True:\n    pass")
    run = run_in_sandbox(cand_dir, '{"op": "is_prime", "args": [2]}', timeout=3.0)
    assert run.output is None
    assert "timeout" in run.raw.get("error", "")
    # the slot must be immediately reusable — no leaked container
    assert _containers_matching("crucible-sbx-") == []


def test_unbounded_allocation_is_killed_by_memory_cap(adapter):
    block = "data = []\n" "while True:\n" "    data.append(bytearray(10 * 1024 * 1024))"
    cand_dir = adapter.materialise(block)
    run = run_in_sandbox(cand_dir, '{"op": "is_prime", "args": [2]}', timeout=10.0)
    assert run.output is None
    # killed (OOM, nonzero exit) well before the 10s timeout — host stays responsive
    assert run.wall_time_s < 9.0
    assert _containers_matching("crucible-sbx-") == []


def test_fork_bomb_is_contained_by_pids_limit(adapter):
    block = "import os\n" "while True:\n" "    os.fork()"
    cand_dir = adapter.materialise(block)
    run = run_in_sandbox(cand_dir, '{"op": "is_prime", "args": [2]}', timeout=10.0)
    assert run.output is None
    assert run.wall_time_s < 9.0
    assert _containers_matching("crucible-sbx-") == []
