"""Task 3.1's own verify step: fire N proposals concurrently and confirm
the machine actually saturates — read via Prometheus's
vllm:num_requests_running, not by trusting the code. See PHASE-3.md.

Usage: python -m bench.concurrency_check --n 64 --knee 32
"""

from __future__ import annotations

import argparse
import asyncio
import statistics
import time

import httpx

from harness.proposal import propose_async

PARENT_BLOCK = """    if op == "is_prime":
        n = args[0]
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        raise ValueError(f"unknown op: {op}")"""

TASK_DESCRIPTION = (
    "An if/elif dispatcher body inside def _dispatch(op, args): that branches on op "
    "and returns the computed result for that operation."
)


async def propose_many(n: int, knee: int) -> tuple[list, float]:
    sem = asyncio.Semaphore(knee)

    async def one(i: int):
        async with sem:
            return await propose_async(
                task_description=TASK_DESCRIPTION,
                parent_block=PARENT_BLOCK,
                quality=0.5,
                cost_tokens=0,
                latency=0.1,
                failed_checks=f"is_prime-{i:02d}: needs a faster primality check",
                temperature=0.9,
            )

    t0 = time.perf_counter()
    results = await asyncio.gather(*(one(i) for i in range(n)), return_exceptions=True)
    wall = time.perf_counter() - t0
    return results, wall


async def sample_queue_depth(prometheus_url: str, samples: list[int], interval_s: float = 0.5) -> None:
    """Appends to `samples` in place — a cancelled task's return value is
    unreachable (awaiting a cancelled task raises CancelledError, it
    doesn't hand back local state), so accumulation has to happen via a
    shared object the caller already holds a reference to."""
    async with httpx.AsyncClient() as client:
        while True:
            try:
                r = await client.get(
                    f"{prometheus_url}/api/v1/query",
                    params={"query": 'vllm:num_requests_running{model_name="proposer"}'},
                    timeout=5.0,
                )
                data = r.json()
                results = data.get("data", {}).get("result", [])
                if results:
                    samples.append(int(float(results[0]["value"][1])))
            except Exception as e:
                print(f"  [sampler error: {e!r}]")
            await asyncio.sleep(interval_s)


async def main_async(n: int, knee: int, prometheus_url: str) -> None:
    print(f"Firing {n} concurrent proposals, semaphore={knee}...")
    samples: list[int] = []
    sampler = asyncio.create_task(sample_queue_depth(prometheus_url, samples, interval_s=0.5))

    results, wall = await propose_many(n, knee)
    sampler.cancel()
    try:
        await sampler
    except asyncio.CancelledError:
        pass

    errors = [r for r in results if isinstance(r, Exception)]
    ok = [r for r in results if not isinstance(r, Exception)]
    total_tokens = sum(t for _, t, _ in ok)
    # completion_tokens (2026-09-25): decode-only, not the prompt+completion
    # total_tokens above - this is what made this exact script's "aggregate
    # tok/s" the source of the untrustworthy 437.8 figure task 3.1's own
    # caveat in TODO.md already flagged (total_tokens far exceeds real
    # decode output, so tok/s computed from it reads high).
    completion_tokens = sum(c for _, _, c in ok)

    print(f"\nCompleted {len(ok)}/{n} in {wall:.1f}s ({len(errors)} errors)")
    if errors:
        print("first error:", repr(errors[0])[:300])
    print(f"total tokens (prompt+completion): {total_tokens}, naive tok/s: {total_tokens / wall:.1f}")
    print(f"completion tokens only: {completion_tokens}, real aggregate tok/s: {completion_tokens / wall:.1f}")
    if samples:
        print(f"\nqueue depth samples: n={len(samples)}")
        print(f"  max:    {max(samples)}")
        print(f"  mean:   {statistics.mean(samples):.1f}")
        print(f"  median: {statistics.median(samples)}")
        print(f"  samples: {samples}")
    else:
        print("\nNo queue depth samples collected — check Prometheus is reachable.")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=64)
    p.add_argument("--knee", type=int, default=32)
    p.add_argument("--prometheus-url", default="http://localhost:9090")
    args = p.parse_args()
    asyncio.run(main_async(args.n, args.knee, args.prometheus_url))


if __name__ == "__main__":
    main()
