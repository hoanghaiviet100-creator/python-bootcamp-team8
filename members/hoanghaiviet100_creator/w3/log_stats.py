import math
from collections import Counter, defaultdict


def _calculate_p95(latencies: list[float]) -> float:
    """Calculate the 95th percentile value from a list of latencies."""
    if not latencies:
        return 0.0
    sorted_lat = sorted(latencies)
    idx = max(0, math.ceil(0.95 * len(sorted_lat)) - 1)
    return float(sorted_lat[idx])


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Analyse chat log route latencies.

    Returns a dict with request counts, p95 latency per route,
    and the route with the highest p95 latency.
    """
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    route_latencies: dict[str, list[float]] = defaultdict(list)
    counts: Counter[str] = Counter()

    for route, latency in pairs:
        counts[route] += 1
        route_latencies[route].append(latency)

    p95_dict: dict[str, float] = {
        route: _calculate_p95(lats) for route, lats in route_latencies.items()
    }

    slowest_route = max(p95_dict, key=p95_dict.get) if p95_dict else None

    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route,
    }