def word_count(text: str) -> dict[str, int]:
    text_lower = text.lower()

    for p in ".,!?:;":
        text_lower = text_lower.replace(p, "")

    words = text_lower.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    return sorted_words[:k]


