"""Summarise request counts and nearest-rank p95 latency by route."""

from collections import Counter, defaultdict
from collections.abc import Iterable
from math import isfinite
from typing import TypedDict


class LogStats(TypedDict):
    """Per-route request counts, p95 latencies, and the slowest route."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: Iterable[tuple[str, float]]) -> LogStats:
    """Return counts, p95, and the route with the highest p95.

    P95 uses the nearest-rank definition: sorted sample ceil(0.95 * n).
    Ties select the first encountered route. Empty input has no slowest route.
    Latencies must be finite and non-negative; invalid values raise ValueError.
    """
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[float]] = defaultdict(list)
    for route, latency_ms in pairs:
        if not isfinite(latency_ms) or latency_ms < 0:
            raise ValueError("Latency must be finite and non-negative")
        counts[route] += 1
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}
    for route, values in latencies.items():
        values.sort()
        rank = (95 * len(values) + 99) // 100
        p95[route] = values[rank - 1]

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": max(p95, key=p95.__getitem__) if p95 else None,
    }
