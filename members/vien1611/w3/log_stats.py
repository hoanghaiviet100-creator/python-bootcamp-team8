"""Log analysis utilities for HTTP route metrics."""

import math
from collections import Counter, defaultdict
from collections.abc import Iterable
from typing import Any


def analyse(pairs: Iterable[tuple[str, float]]) -> dict[str, Any]:
    """Analyse request counts and 95th percentile latency per route.

    Parameters
    ----------
    pairs : Iterable[tuple[str, float]]
        A sequence or iterable of (route, latency_ms) tuples.

    Returns
    -------
    dict[str, Any]
        A dictionary containing:
        - "counts": Counter mapping each route to request count
        - "p95": dict mapping each route to its 95th percentile latency
        - "slowest": the route name with the highest p95 latency (or None if empty)
    """
    counts: Counter[str] = Counter()
    route_latencies: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        route_latencies[route].append(float(latency))

    p95: dict[str, float] = {}
    for route, latencies in route_latencies.items():
        sorted_vals = sorted(latencies)
        index = math.ceil(0.95 * len(sorted_vals)) - 1
        p95[route] = sorted_vals[index]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
