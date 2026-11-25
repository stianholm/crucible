"""Deterministic task-set split. See PHASE-1.md task 1.2.

Hash the item id and bucket on the hash, never a random shuffle with an
unrecorded seed, so the split can be rebuilt byte-identically from this
rule alone.
"""

from __future__ import annotations

import hashlib


def split_of(item_id: str) -> str:
    h = int(hashlib.sha256(item_id.encode()).hexdigest()[:8], 16) % 100
    if h < 10:
        return "dev"
    if h < 55:
        return "rotation"
    return "held_out"
