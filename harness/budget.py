"""The budget governor. See PHASE-2.md task 2.6.

Three hard caps, three stop conditions, all read from config rather than
hardcoded. The run must stop by itself — that's the exit criterion for
this phase being unattended.
"""

from __future__ import annotations

import time
from dataclasses import dataclass


@dataclass
class Budget:
    max_iterations: int = 50
    max_tokens: int = 2_000_000
    max_wall_s: float = 4 * 3600
    patience: int = 12

    _start: float = 0.0
    _tokens_used: int = 0
    _iteration: int = 0

    def __post_init__(self) -> None:
        self._start = time.perf_counter()

    def iterations(self):
        while True:
            if self.exhausted():
                return
            yield self._iteration
            self._iteration += 1

    def spend_tokens(self, n: int) -> None:
        self._tokens_used += n

    def exhausted(self) -> tuple[bool, str] | bool:
        if self._iteration >= self.max_iterations:
            return True
        if self._tokens_used >= self.max_tokens:
            return True
        if time.perf_counter() - self._start >= self.max_wall_s:
            return True
        return False

    def exhaustion_reason(self) -> str | None:
        if self._iteration >= self.max_iterations:
            return f"max_iterations ({self.max_iterations})"
        if self._tokens_used >= self.max_tokens:
            return f"max_tokens ({self.max_tokens})"
        if time.perf_counter() - self._start >= self.max_wall_s:
            return f"max_wall_s ({self.max_wall_s})"
        return None

    @property
    def elapsed_s(self) -> float:
        return time.perf_counter() - self._start

    @property
    def tokens_used(self) -> int:
        return self._tokens_used

    @property
    def iteration_count(self) -> int:
        return self._iteration
