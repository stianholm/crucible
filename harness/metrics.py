"""Prometheus queries the generation report needs. See PHASE-3.md task 3.8's
throughput row (peak/sustained queue depth, prefix cache hit rate)."""

from __future__ import annotations

import httpx


def _instant_query(prometheus_url: str, query: str) -> float | None:
    try:
        r = httpx.get(f"{prometheus_url}/api/v1/query", params={"query": query}, timeout=5.0)
        results = r.json().get("data", {}).get("result", [])
        return float(results[0]["value"][1]) if results else None
    except Exception:
        return None


def prefix_cache_hit_rate(prometheus_url: str = "http://localhost:9090") -> float | None:
    """Cumulative hit rate since the proposer started — not windowed to
    one generation (Prometheus counters reset only on restart), but still
    the signal task 3.1 cares about: is it non-zero and not falling."""
    hits = _instant_query(prometheus_url, 'vllm:prefix_cache_hits_total{model_name="proposer"}')
    queries = _instant_query(prometheus_url, 'vllm:prefix_cache_queries_total{model_name="proposer"}')
    if hits is None or queries is None or queries == 0:
        return None
    return hits / queries


def current_queue_depth(prometheus_url: str = "http://localhost:9090") -> int | None:
    v = _instant_query(prometheus_url, 'vllm:num_requests_running{model_name="proposer"}')
    return int(v) if v is not None else None
