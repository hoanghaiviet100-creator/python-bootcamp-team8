def word_count(text: str) -> dict[str, int]:
    # 1. Chuyển toàn bộ văn bản về chữ thường
    text_lower = text.lower()

    # 2. Loại bỏ các dấu câu: . , ! ? ; :
    for p in ".,!?:;":
        text_lower = text_lower.replace(p, "")

    # 3. Tách văn bản thành danh sách các từ
    words = text_lower.split()

    # 4. Đếm số lần xuất hiện của từng từ
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    # 1. Lấy dictionary thống kê từ hàm word_count
    counts = word_count(text)

    # 2. Sắp xếp danh sách (word, count):
    # - -x[1]: số lần xuất hiện giảm dần
    # - x[0]: từ sắp xếp theo bảng chữ cái A-Z
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # 3. Lấy k phần tử đầu tiên
    return sorted_words[:k]


# --- Đoạn test thử ---
if __name__ == "__main__":
    sample_text = "Git is fun. Git is fast!"

    print("Word count:", word_count(sample_text))
    print("Top 2:", top_k(sample_text, 2))