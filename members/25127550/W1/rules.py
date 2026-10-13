import string
from collections import Counter

def word_count(text: str) -> dict[str, int]:
    # Chuyển về chữ thường và loại bỏ dấu câu
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, " ")
    
    words = text.split()
    counts = Counter(words)
    return dict(counts)

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    # Sắp xếp theo số lượng giảm dần, sau đó theo từ tăng dần (alphabet)
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:k]