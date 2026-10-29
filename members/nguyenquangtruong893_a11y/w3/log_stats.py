"""W3-2: Chat log analytics - request counts, p95 latency, and slowest route."""

import math
from collections import Counter, defaultdict
from typing import Any


def _calc_p95(values: list[float]) -> float:
    """Compute the 95th percentile latency using the nearest-rank method."""
    if not values:
        return 0.0
    sorted_values = sorted(values)
    # 95th percentile index calculation (1-based ceiling mapped to 0-based index)
    rank = math.ceil(0.95 * len(sorted_values))
    idx = max(0, min(rank - 1, len(sorted_values) - 1))
    return float(sorted_values[idx])


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Analyze route requests and latencies.

    Args:
        pairs: List of tuples (route_name, latency_in_ms).

    Returns:
        dict containing:
        - "counts": Counter mapping route to request count.
        - "p95": dict mapping route to 95th percentile latency.
        - "slowest": route name with the highest p95 latency (None if pairs is empty).
    """
    if not pairs:
        return {
            "counts": Counter(),
            "p95": {},
            "slowest": None,
        }

    counts: Counter[str] = Counter()
    route_latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        route_latencies[route].append(float(latency))

    p95_dict: dict[str, float] = {
        route: _calc_p95(latencies) for route, latencies in route_latencies.items()
    }

    # Identify the route with maximum p95 latency
    slowest_route = max(p95_dict.items(), key=lambda item: item[1])[0]

    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route,
    }
