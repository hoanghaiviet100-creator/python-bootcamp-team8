
def word_count(text: str) -> dict[str, int]:
    """
    Đếm số lần xuất hiện của từng từ trong chuỗi:
    - Chuyển văn bản thành chữ viết thường (lower-case).
    - Loại bỏ các dấu câu: . , ! ? ; :.
    """
    punctuation = ".,!?;:"
    for p in punctuation:
        text = text.replace(p, "")
        
    words = text.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """
    Trả về danh sách k từ xuất hiện nhiều nhất dạng tuple (từ, số_lần):
    - Ưu tiên sắp xếp giảm dần theo số lần xuất hiện.
    - Nếu bằng số lần, sắp xếp tăng dần theo bảng chữ cái của từ[cite: 5].
    """
    counts = word_count(text)
    
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    return sorted_items[:k]


