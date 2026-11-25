"""Shared types for the solution adapter contract. See PHASE-1.md task 1.1."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Task:
    """One item from a solution's task set (dev/rotation/held_out)."""

    task_id: str
    input: str
    expected: Any = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Run:
    """The result of invoking a candidate on one task."""

    output: Any
    tokens: int
    tool_calls: int
    wall_time_s: float
    raw: dict[str, Any] = field(default_factory=dict)
