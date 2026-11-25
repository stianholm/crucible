"""Scale the Phase 2 single slot to a pool. See PHASE-3.md task 3.5.

Sized from measurements, not intuition: slots = min(sandbox_memory_budget
/ per_sandbox_memory, (cpu_cores - cores_reserved_for_vllm) / cores_per_sandbox).

The spec's own worked example assumes a 2 GB/sandbox cap; this fixture's
candidates need nowhere near that (harness.sandbox already defaults to
256 MB), so DEFAULT_SLOTS here is sized off the real numbers in
docs/platform.md/CAPACITY.yaml for this machine, not copied from the spec's
illustrative figure. Re-derive it if the per-sandbox memory cap or
available headroom changes meaningfully.

Uses a thread pool, not asyncio, for the sandbox side: each `docker run`
is a blocking subprocess call, and Python releases the GIL for the
syscall wait, so N worker threads genuinely run N containers
concurrently — no need to rewrite harness.sandbox around
asyncio.create_subprocess_exec for this to be real concurrency, the way
task 3.1 needed for the proposer's HTTP calls.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeoutError
from pathlib import Path

from harness.adapter import SolutionAdapter
from harness.fitness import Fitness
from harness.scorer import evaluate
from harness.types import Task

DEFAULT_SLOTS = 8  # see module docstring — sized for this machine's real headroom, not the spec's 2GB example

# harness.sandbox enforces its wall clock twice on purpose — in-container,
# and a parent-process backstop, because relying on one layer alone is
# fragile (see that module's docstring). This pool had only one layer:
# evaluate()'s own internal timeout (adapter.eval_timeout_s, or
# MAX_WALL_S). A stuck backend (an unresponsive judge engine, a network
# call that never returns) could occupy a slot indefinitely with nothing
# here to notice. Found by the session-review workflow, 2026-09-22.
# BACKSTOP_TIMEOUT_S is generous slack over the largest documented adapter
# eval_timeout_s (capability_case: 900s) — this is a caller-side give-up,
# not a true kill: Python can't forcibly stop a running thread the way
# `docker kill` stops a container, so the stuck thread keeps running until
# it finishes or the process exits. What this buys is that the pool
# doesn't wait on it forever — one slow candidate no longer blocks an
# entire generation's evaluation batch.
BACKSTOP_TIMEOUT_S = 1200.0


class SandboxPool:
    def __init__(self, slots: int = DEFAULT_SLOTS):
        self.slots = slots
        self._executor = ThreadPoolExecutor(max_workers=slots, thread_name_prefix="sandbox-slot")

    def evaluate_many(
        self,
        adapter: SolutionAdapter,
        cand_dirs: list[Path],
        tasks: list[Task],
    ) -> list:
        """cand_dirs and tasks must be the same length — one (candidate,
        task) pair per element, evaluated concurrently across the pool."""
        assert len(cand_dirs) == len(tasks)
        futures = [
            self._executor.submit(evaluate, adapter, cand_dir, task)
            for cand_dir, task in zip(cand_dirs, tasks)
        ]
        results = []
        for f in futures:
            try:
                results.append(f.result(timeout=BACKSTOP_TIMEOUT_S))
            except FutureTimeoutError:
                results.append(
                    Fitness(
                        valid=False,
                        quality=0.0,
                        cost_tokens=0,
                        latency_s=BACKSTOP_TIMEOUT_S,
                        descriptors=(0, 0),
                        detail={"gate": "pool_backstop_timeout"},
                    )
                )
        return results

    def shutdown(self) -> None:
        self._executor.shutdown(wait=True)

    def __enter__(self) -> "SandboxPool":
        return self

    def __exit__(self, *exc) -> None:
        self.shutdown()
