"""The solution adapter contract. See PHASE-1.md task 1.1.

Everything the harness needs from a solution, and nothing about how the
solution works. A solution is onboarded by implementing this Protocol —
the harness never imports a solution's internals directly.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol

from harness.types import Run, Task


class SolutionAdapter(Protocol):
    solution_id: str
    executes_code: bool  # answer to onboarding question 7, selects the evaluator

    def materialise(self, block: str) -> Path:
        """Frozen scaffolding plus the proposed block, in a fresh directory."""
        ...

    def invoke(self, cand: Path, task_input: str, timeout: float) -> Run:
        """Run one task. Returns output, tokens, tool calls, wall time."""
        ...

    def shape_ok(self, output: Any) -> bool:
        """Cheap gate. Is this the right kind of thing at all."""
        ...

    def programmatic_checks(self, output: Any, task: Task) -> dict[str, tuple[float, str]]:
        """Deterministic scoring. {name: (score 0..1, evidence)}."""
        ...

    def needs_judgement(self, task: Task) -> bool:
        """Whether the expensive tier runs for this task at all."""
        ...

    def descriptors(self, run: Run) -> tuple[int, int]:
        """Archive coordinates. See PHASE-1.md task 1.3."""
        ...
