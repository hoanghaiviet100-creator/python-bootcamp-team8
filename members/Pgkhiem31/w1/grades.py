def summary(scores : list[float]) -> dict:
    if not scores:
        raise ValueError("The scores list is empty.")

    sorted_scores = sorted(scores)
    n = len(scores)
    mean = sum(scores)/n
    if(n % 2 == 1):
        median = sorted_scores[n//2]
    else:
        median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2


    return{
        "min" : min(scores) , 
        "max" : max(scores) ,
        "mean" : round(mean , 2),
        "median" : round(median , 2)}