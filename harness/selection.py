"""Parent selection. See PHASE-3.md task 3.4.

Selecting the best elite every time is hill climbing with extra
infrastructure — it will lose the equal-budget test (task 3.9) against
Phase 2's plain hill climber. This is where population search has to
actually earn its keep: exploit the best, explore broadly, and push the
frontier where the archive is still empty.
"""

from __future__ import annotations

import random

import psycopg

from harness.archive import cells, cells_adjacent_to_empty


def select_parents(
    conn: psycopg.Connection,
    solution_id: str,
    island_id: int,
    n: int,
    grid_dims: tuple[int, int],
    seed_block: str,
    rng: random.Random | None = None,
) -> list[dict]:
    """Returns n dicts, each either {"block": seed_block, "iteration_id":
    None} (empty island, nothing to select from yet) or an elite cell dict
    from harness.archive.cells()."""
    rng = rng or random.Random()
    occupied = cells(conn, solution_id, island_id)
    if not occupied:
        return [{"block": seed_block, "iteration_id": None, "root_sha": None} for _ in range(n)]

    elites = sorted(occupied, key=lambda c: c["scalar"], reverse=True)
    top = elites[: max(1, len(elites) // 4)]
    frontier = cells_adjacent_to_empty(conn, solution_id, island_id, grid_dims) or occupied

    picks = []
    for _ in range(n):
        r = rng.random()
        if r < 0.60:
            picks.append(rng.choice(top))  # exploit
        elif r < 0.85:
            picks.append(rng.choice(occupied))  # explore
        else:
            picks.append(rng.choice(frontier))  # push the frontier
    return picks


def inspirations(occupied: list[dict], exclude_iteration_id: int | None, k: int = 3) -> list[dict]:
    """A handful of other elites to include alongside the parent, so the
    proposer can recombine material it can otherwise never see. See task
    3.4 — most of what makes evolutionary search outperform repeated
    mutation is recombination, and the model can only recombine what's in
    its context."""
    pool = [c for c in occupied if c["iteration_id"] != exclude_iteration_id]
    if len(pool) <= k:
        return pool
    return random.sample(pool, k)
