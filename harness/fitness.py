"""FROZEN. See PHASE-1.md task 1.3. A candidate must never import or modify
this file — it lives outside the mutation surface entirely.

Objectives and descriptors are different things. Objectives are what the
search maximises. Descriptors are archive coordinates and are never
optimised. Mixing them means the search starts gaming the diversity
mechanism that exists to protect it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

COST_REF_TOKENS = 4000  # normalisation anchor, not a cap
LAT_REF_S = 10.0
LAMBDA_COST = 0.10
LAMBDA_LAT = 0.05


@dataclass(frozen=True)
class Fitness:
    valid: bool  # hard gate: did it run at all
    quality: float  # 0..1, the primary objective
    cost_tokens: int  # objective, minimised
    latency_s: float  # objective, minimised
    descriptors: tuple[int, int]  # archive cell. NOT optimised.
    detail: dict[str, Any] = field(default_factory=dict)  # evidence for Phase 4

    @property
    def scalar(self) -> float:
        """Only for Phase 2 hill climbing. Phase 3 ranks on the vector."""
        if not self.valid:
            return 0.0
        return (
            self.quality
            - LAMBDA_COST * min(self.cost_tokens / COST_REF_TOKENS, 2.0)
            - LAMBDA_LAT * min(self.latency_s / LAT_REF_S, 2.0)
        )
