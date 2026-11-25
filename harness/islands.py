"""Islands and migration. See PHASE-3.md task 3.3.

Four islands, each with its own grid — a single population converges onto
one lineage within roughly ten generations and reports steady, meaningless
progress, which is exactly the failure this structure exists to prevent.

Migration runs every fifth generation only. Migrating every generation
defeats the purpose: one population with extra bookkeeping, and the
collapse arrives on schedule anyway.
"""

from __future__ import annotations

import psycopg

from harness.archive import best_elite, try_insert

N_ISLANDS = 4
MIGRATION_INTERVAL = 5


def should_migrate(generation: int) -> bool:
    return generation > 0 and generation % MIGRATION_INTERVAL == 0


def migrate(conn: psycopg.Connection, solution_id: str, n_islands: int = N_ISLANDS) -> list[dict]:
    """Copies each island's single best elite into the next island around
    a ring (0->1->2->3->0). Returns a log of what migrated where."""
    bests = {i: best_elite(conn, solution_id, i) for i in range(n_islands)}
    log = []
    for src in range(n_islands):
        elite = bests[src]
        if elite is None:
            continue
        dst = (src + 1) % n_islands
        claimed = try_insert(conn, solution_id, dst, elite["cell"], elite["iteration_id"], elite["scalar"])
        log.append(
            {
                "from_island": src,
                "to_island": dst,
                "cell": elite["cell"],
                "scalar": elite["scalar"],
                "claimed": claimed,
            }
        )
    return log
