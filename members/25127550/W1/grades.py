def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("List cannot be empty")
    
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    
    min_val = sorted_scores[0]
    max_val = sorted_scores[-1]
    mean_val = round(sum(scores) / n, 2)
    
    if n % 2 == 1:
        median_val = sorted_scores[n // 2]
    else:
        median_val = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
    
    median_val = round(median_val, 2)
    
    return {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "median": median_val
    }