"""The plateau ladder. See PHASE-6.md, "Plateau handling".

Detection: no held-out improvement above one sigma for PLATEAU_GENS
generations. Then four steps, in order, each recorded as an event:

1. Widen mutation temperature on all islands.
2. Reseed the weakest island from an early archive snapshot.
3. Request an off-cycle distillation round.
4. Dormant: release the GPU and wait for a human decision.

Step four holds. It never loops back to step one by itself: only a held-out
gain (impossible while dormant) or a new eval set restarts the climb, which is
exactly PHASE-6.md's re-entry rule ("plateaued, eval set just rotated:
re-enters contention").

The state is replayed from the event log rather than stored, so it cannot
drift from what the morning report shows: both read the same rows.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass

PLATEAU_GENS = 12       # PHASE-6.md's opening value
SIGMA_FLOOR = 0.01      # default; a solution with measured noise sets its own (BASELINE.yaml ladder.sigma_floor)
DORMANT = 4
STEPS = {
    1: "widen mutation temperature",
    2: "reseed the weakest island from the original seed",
    3: "request an off-cycle distillation round",
    4: "dormant: GPU released, waiting for a human decision",
}


@dataclass
class LadderState:
    eval_version: str
    best: float | None = None
    since: int = 0     # generations since the last held-out gain or ladder step
    step: int = 0

    @property
    def dormant(self) -> bool:
        return self.step >= DORMANT

    @property
    def due(self) -> int | None:
        """The step to take now, or None."""
        if self.dormant or self.since < PLATEAU_GENS:
            return None
        return self.step + 1


def sigma(passes: list[float], floor: float = SIGMA_FLOOR) -> float:
    return max(floor, statistics.stdev(passes) if len(passes) > 1 else 0.0)


def replay(events: list[dict], eval_version: str, sigma_floor: float = SIGMA_FLOOR) -> LadderState:
    """events: this solution's held_out and ladder events, oldest first.
    Events from another eval set are ignored, so a rotation starts clean."""
    st = LadderState(eval_version)
    for e in events:
        d = e["detail"]
        if d.get("eval_version") != eval_version:
            continue
        if e["kind"] == "held_out":
            q = d["quality"]
            if st.best is None or q > st.best + sigma(d.get("passes") or [q], sigma_floor):
                st.best, st.since, st.step = q, 0, 0
            else:
                st.since += int(d.get("generations") or 0)
        elif e["kind"] == "ladder":
            st.step, st.since = int(d["step"]), 0
    return st
