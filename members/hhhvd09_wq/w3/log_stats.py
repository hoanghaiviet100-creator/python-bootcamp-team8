"""Analyse request counts and latency by route."""

from collections import Counter, defaultdict
from math import ceil


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, object]:
    """Compute counts, nearest-rank p95 latencies, and the slowest route."""
    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[int | float]] = defaultdict(list)
    for route, latency_ms in pairs:
        counts[route] += 1
        latencies[route].append(latency_ms)
    p95: dict[str, int | float] = {}
    for route, values in latencies.items():
        ordered = sorted(values)
        p95[route] = ordered[ceil(0.95 * len(ordered)) - 1]
    slowest = max(p95, key=p95.__getitem__) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
