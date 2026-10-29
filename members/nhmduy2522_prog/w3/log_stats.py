import math
from collections import Counter, defaultdict
from typing import Any


def calculate_p95(latencies: list[float]) -> float:
    """Calculate the 95th percentile (p95) latency using nearest-rank method."""
    if not latencies:
        return 0.0
    sorted_latencies = sorted(latencies)
    # Nearest-rank percentile formula: k = ceil(0.95 * N)
    index = math.ceil(0.95 * len(sorted_latencies)) - 1
    return float(sorted_latencies[index])


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Analyse request log pairs and return counts, p95 latencies, and the slowest route.

    Args:
        pairs: A list of (route, latency_ms) tuples.

    Returns:
        A dict with keys 'counts', 'p95', and 'slowest'.
    """
    counts = Counter()
    route_latencies = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        route_latencies[route].append(latency)

    p95_dict = {
        route: calculate_p95(latencies)
        for route, latencies in route_latencies.items()
    }

    slowest_route = max(p95_dict, key=p95_dict.get) if p95_dict else None

    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route,
    }