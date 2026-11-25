"""The MAP-Elites archive. See PHASE-3.md task 3.2 and 3.6.

A candidate claims its cell if the cell is empty or it beats the current
occupant. Grid sizing sets selection pressure — the fixture's own
descriptors (output length bin, runtime bin, each 0-5) already give a 6x6
grid per island, landing right in the spec's own "two to four times the
generation size" sweet spot for 16 candidates/island.
"""

from __future__ import annotations

import psycopg


def try_insert(
    conn: psycopg.Connection,
    solution_id: str,
    island_id: int,
    cell: tuple[int, int],
    iteration_id: int,
    scalar: float,
) -> bool:
    """Returns True if the candidate claimed or improved the cell."""
    # psycopg infers a bare Python list of small ints as smallint[], but
    # the `cell` column is int[] — without the explicit cast, postgres
    # refuses the comparison with "operator does not exist: integer[] =
    # smallint[]" rather than silently coercing it.
    cell_list = list(cell)
    with conn.cursor() as cur:
        cur.execute(
            "select scalar from elite where solution_id = %s and island_id = %s and cell = %s::int[]",
            (solution_id, island_id, cell_list),
        )
        row = cur.fetchone()
        if row is not None and row[0] >= scalar:
            return False
        cur.execute(
            """
            insert into elite (solution_id, island_id, cell, iteration_id, scalar)
            values (%s, %s, %s::int[], %s, %s)
            on conflict (solution_id, island_id, cell) do update
              set iteration_id = excluded.iteration_id,
                  scalar       = excluded.scalar,
                  updated_at   = now()
            """,
            (solution_id, island_id, cell_list, iteration_id, scalar),
        )
    conn.commit()
    return True


def cells(conn: psycopg.Connection, solution_id: str, island_id: int) -> list[dict]:
    with conn.cursor() as cur:
        cur.execute(
            """
            select e.cell, e.scalar, e.iteration_id, i.root_sha, i.candidate_sha
            from elite e join iteration i on i.id = e.iteration_id
            where e.solution_id = %s and e.island_id = %s
            """,
            (solution_id, island_id),
        )
        return [
            {
                "cell": tuple(row[0]),
                "scalar": row[1],
                "iteration_id": row[2],
                "root_sha": row[3],
                "candidate_sha": row[4],
            }
            for row in cur.fetchall()
        ]


def coverage(conn: psycopg.Connection, solution_id: str, island_id: int, grid_size: int) -> float:
    """Fraction of cells occupied. Falling coverage means convergence."""
    return len(cells(conn, solution_id, island_id)) / grid_size


def qd_score(conn: psycopg.Connection, solution_id: str, island_id: int) -> float:
    """Sum of best scalar per occupied cell. Rises with quality AND spread."""
    return sum(c["scalar"] for c in cells(conn, solution_id, island_id))


def unique_ancestors(conn: psycopg.Connection, solution_id: str, island_id: int) -> int:
    """Distinct lineage roots among current elites. The collapse detector."""
    return len({c["root_sha"] for c in cells(conn, solution_id, island_id) if c["root_sha"]})


def best_elite(conn: psycopg.Connection, solution_id: str, island_id: int) -> dict | None:
    occupied = cells(conn, solution_id, island_id)
    if not occupied:
        return None
    return max(occupied, key=lambda c: c["scalar"])


def cells_adjacent_to_empty(
    conn: psycopg.Connection, solution_id: str, island_id: int, grid_dims: tuple[int, int]
) -> list[dict]:
    """Occupied cells with at least one empty 4-neighbour — the frontier
    parent selection (task 3.4) pushes outward from."""
    occupied = cells(conn, solution_id, island_id)
    occupied_coords = {c["cell"] for c in occupied}
    w, h = grid_dims
    frontier = []
    for c in occupied:
        x, y = c["cell"]
        neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        neighbours = [(nx, ny) for nx, ny in neighbours if 0 <= nx < w and 0 <= ny < h]
        if any(n not in occupied_coords for n in neighbours):
            frontier.append(c)
    return frontier
