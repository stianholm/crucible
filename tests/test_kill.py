"""The kill switch's process matching and the halt flag (PHASE-6.md)."""

import importlib.util
from pathlib import Path

from harness.halt import halted

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("kill", REPO / "ops" / "kill.py")
kill = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kill)


def test_matches_runs_by_resolved_path():
    r = str(REPO)
    assert kill.is_run(["bash", "ops/search.sh", "s5", "10"], r) == "ops/search.sh"
    assert kill.is_run(["bash", f"{r}/ops/nightly.sh"], "/") == "ops/nightly.sh"
    assert kill.is_run([".venv/bin/python", "-"], r) == "python"
    assert kill.is_run([f"{r}/.venv/bin/python", "-m", "pytest"], "/tmp") == "python"


def test_ignores_text_that_merely_mentions_a_run():
    r = str(REPO)
    # the pkill -f mistake: a shell whose command string names the script
    assert kill.is_run(["/bin/bash", "-c", "tail -f logs/x; ops/search.sh s5"], r) is None
    assert kill.is_run(["grep", "ops/search.sh", "logs/x"], r) is None
    # someone else's venv, or the same relative path from another directory
    assert kill.is_run([".venv/bin/python", "-"], "/home/other/project") is None
    assert kill.is_run([], r) is None


def test_halt_flag(tmp_path):
    f = tmp_path / "HALT"
    assert halted(f) is None
    f.write_text("2026-10-24T09:00:00 plateau step 4 (by stian)\n")
    assert halted(f) == "2026-10-24T09:00:00 plateau step 4 (by stian)"
    f.write_text("")
    assert halted(f) == "halted (no reason recorded)"
