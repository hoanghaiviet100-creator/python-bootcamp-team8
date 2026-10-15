def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Danh sách điểm không được để trống")
    
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    
    if n % 2 == 1:
        median = sorted_scores[n // 2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
        
    result = {
        "min": min(scores),
        "max": max(scores),
        "mean": round(sum(scores) / n, 2),
        "median": round(median, 2)
    }
    return result