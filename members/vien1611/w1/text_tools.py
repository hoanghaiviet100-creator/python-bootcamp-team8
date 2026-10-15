def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    for punctuation in ".,!?;:":
        text = text.replace(punctuation, "")
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]

result = top_k("Git is fun. Git is fast!", 2)
print(result)