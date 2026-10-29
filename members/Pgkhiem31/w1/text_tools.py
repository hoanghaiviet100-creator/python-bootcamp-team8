#text_tools.py
def word_count(text: str) -> dict[str, int]:
    """Count lowercase whitespace-separated words after removing .,!?;:."""
    ignore = str.maketrans("", "", ".,!?;:")
    text = text.translate(ignore).lower()
    words = text.split()
    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return up to k words by descending count, then alphabetical order.

    Non-positive k values return an empty list.
    """
    if k <= 0:
        return []

    counts = word_count(text)

    sorted_words = sorted(counts.items(), key=lambda items: (-items[1], items[0]))

    return sorted_words[:k]
