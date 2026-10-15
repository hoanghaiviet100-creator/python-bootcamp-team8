import statistics


def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("The scores list cannot be empty.")

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2),
    }


if __name__ == "__main__":
    raw_input = input("Enter scores (e.g. 7.5 9 6 8): ")

    try:
        test_scores = [float(x) for x in raw_input.split()]
        output = summary(test_scores)
        print("Result:", output)
    except ValueError as e:
        print("Error:", e)