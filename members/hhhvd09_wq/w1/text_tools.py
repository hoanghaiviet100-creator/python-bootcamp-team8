def word_count(text: str) -> dict[str, int]:
    """Count words case-insensitively without basic punctuation."""
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
    """Return common words sorted by count and alphabetical tie break."""
    counts = word_count(text)

    sorted_words = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    return sorted_words[:max(k, 0)]
