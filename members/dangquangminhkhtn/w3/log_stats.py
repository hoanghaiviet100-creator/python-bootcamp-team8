from collections import Counter
import math


def analyse(pairs) -> dict:
    counts = Counter()
    latencies = {}

    for route, latency in pairs:
        counts[route] += 1

        if route not in latencies:
            latencies[route] = []

        latencies[route].append(latency)

    p95 = {}

    for route in latencies:
        values = sorted(latencies[route])
        index = math.ceil(0.95 * len(values)) - 1
        p95[route] = values[index]

    slowest = max(p95, key=p95.get) if p95 else None

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest
    }
