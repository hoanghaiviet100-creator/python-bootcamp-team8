import string 
def word_count(text: str) -> dict[str, int]:
    ignore = str.maketrans("", "", ".,!?;:")
    text = text.translate(ignore).lower()
    words = text.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts

def top_k(text : str , k : int) -> list[tuple[str , int]]:
    if k <= 0:
        return []

    counts = word_count(text)

    sorted_words = sorted(counts.items() , key = lambda items: ( -items[1] , items[0]))

    return sorted_words[:k]