"""Text analysis utility functions."""


def word_count(text: str) -> dict[str, int]:
    """Count occurrences of each word in a string, ignoring punctuation and case."""
    text = text.lower()
    for punctuation in ".,!?;:":
        text = text.replace(punctuation, "")
    words = text.split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k most frequent words sorted by frequency (descending) and word (alphabetical)."""
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]


if __name__ == "__main__":
    result = top_k("Git is fun. Git is fast!", 2)
    print(result)
