import string
from collections import Counter

def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, " ")
    
    words = text.split()
    counts = Counter(words)
    return dict(counts)

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:k]