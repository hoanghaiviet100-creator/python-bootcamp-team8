"""Grade summary utility functions."""


def summary(score: list[float]) -> dict[str, float]:
    """Calculate summary statistics (min, max, mean, median) for a list of scores."""
    if not score:
        raise ValueError("score cannot be empty")

    total = sum(score)
    average = total / len(score)
    temp_list = score.copy()
    temp_list.sort()
    if len(temp_list) % 2 == 0:
        temp_median = (
            temp_list[len(temp_list) // 2 - 1] + temp_list[len(temp_list) // 2]
        ) / 2
    else:
        temp_median = temp_list[len(temp_list) // 2]

    result = {
        "min": temp_list[0],
        "max": temp_list[-1],
        "mean": round(average, 2),
        "median": round(temp_median, 2),
    }
    return result


if __name__ == "__main__":
    score = [7.5, 9, 6, 8]
    print(summary(score))
