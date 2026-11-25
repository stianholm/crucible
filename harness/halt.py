"""The halt flag behind the kill switch. See PHASE-6.md, "The kill switch".

`ops/kill.py` writes state/HALT and stops whatever is running. The flag is
what keeps it stopped: run_population checks it before every generation, and
the scheduler refuses to start anything while it exists. Clearing it is a
deliberate human act (`ops/kill.py --clear`), never something the system does
for itself, because a halt is the ladder's step four as well as the operator's
emergency stop, and both mean "wait for a person".
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HALT_FILE = REPO_ROOT / "state" / "HALT"


def halted(path: Path = HALT_FILE) -> str | None:
    """The recorded reason if the harness is halted, else None."""
    try:
        return path.read_text().strip() or "halted (no reason recorded)"
    except FileNotFoundError:
        return None
