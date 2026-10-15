def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Scores must not be empty!")

    ordered = sorted(scores)
    n = len(ordered)

    minimum = min(scores)
    maximum = max(scores)
    mean = round(sum(scores) / n, 2)

    if n % 2 == 0:
        median = round(
            (ordered[n // 2 - 1] + ordered[n // 2]) / 2, 2
        )
    else:
        median = round(ordered[n // 2], 2)

    return {
        "min": minimum,
        "max": maximum,
        "mean": mean,
        "median": median
    }