def word_count(text: str) -> dict[str, int]:
    punctuation = ".,!?;:"
    text = text.lower()

    for c in punctuation:
        text = text.replace(c, "")

    words = text.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:max(k, 0)]