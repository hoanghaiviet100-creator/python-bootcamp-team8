
from members.vien1611.w1.grades import summary
from members.vien1611.w1.rules import can_register_thesis, missing
from members.vien1611.w1.text_tools import top_k, word_count
from members.vien1611.w1.timetable import by_day
from members.vien1611.w1.translate import fibonacci_iterative, fibonacci_recursive


# Test 1: Module grades.py
def test_grades_summary_standard_and_single_element():
    """
    Test tính toán min, max, mean, median cho grades.py.
    - Standard case: Danh sách có số lượng phần tử chẵn [7.5, 9, 6, 8]
    - Edge Case: Danh sách chỉ có 1 phần tử [8.5]
    """
    # 1. Standard Case (Chẵn phần tử)
    res = summary([7.5, 9.0, 6.0, 8.0])
    assert res == {
        'min': 6.0,
        'max': 9.0,
        'mean': 7.62,
        'median': 7.75
    }

    # 2. Edge Case: Mảng chỉ có duy nhất 1 điểm số
    res_single = summary([8.5])
    assert res_single == {
        'min': 8.5,
        'max': 8.5,
        'mean': 8.5,
        'median': 8.5
    }


# Test 2: Module rules.py
def test_thesis_rules_exact_boundary_and_float_precision():
    """
    Test kiểm tra điều kiện làm khóa luận.
    - Edge Case 1: Tín chỉ và GPA nằm ĐÚNG NGƯỠNG biên (120 credits, 2.0 GPA)
    - Edge Case 2: Kiểm tra sai số làm tròn số thực khi trừ GPA (2.0 - 1.85 = 0.15)
    """
    assert can_register_thesis(120, 2.0) is True
    assert missing(120, 2.0) == []

    assert can_register_thesis(115, 1.85) is False
    reasons = missing(115, 1.85)
    assert "need 5 more credits" in reasons
    assert "need 0.15 more gpa" in reasons


# Test 3: Module text_tools.py (EDGE CASES ĐẶC BIỆT)
def test_text_tools_edge_cases():
    """
    [EDGE CASE GIẢNG VIÊN THƯỜNG BỎ QUÊN]
    1. Chuỗi CHỈ CHỨA DẤU CÂU (Không có từ nào).
    2. Tham số `k` LỚN HƠN tổng số từ duy nhất có trong văn bản.
    3. Quy tắc ưu tiên sắp xếp theo bảng chữ cái khi tần suất xuất hiện bằng nhau.
    """
    # Edge Case 1: Chuỗi chỉ toàn dấu câu và khoảng trắng
    punct_only = "..., !? ;;"
    assert word_count(punct_only) == {}
    assert top_k(punct_only, k=5) == []

    # Edge Case 2: k = 10 nhưng văn bản chỉ có 2 từ duy nhất
    text = "Git is fast. Git is fun!"
    result_k_large = top_k(text, k=10)
    assert len(result_k_large) == 4
    
    # Edge Case 3: Kiểm tra thứ tự sắp xếp bảng chữ cái khi hòa tần suất
    assert result_k_large[0] == ('git', 2)
    assert result_k_large[1] == ('is', 2)


# Test 4: Module timetable.py
def test_timetable_grouping_and_empty_edge_case():
    """
    Test gộp thời khóa biểu.
    - Standard Case: Gộp môn học, giữ nguyên thứ tự xuất hiện của Thứ và sắp xếp tên môn học.
    - Edge Case: Đầu vào là danh sách rỗng [].
    """
    # Standard Case
    data = [("CSC10014", "Wed"), ("MTH00003", "Tue"), ("CSC10001", "Wed")]
    result = by_day(data)
    
    assert list(result.keys()) == ["Wed", "Tue"]  # Thứ tự thứ xuất hiện lần đầu
    assert result["Wed"] == ["CSC10001", "CSC10014"]  # Đã sắp xếp tên môn học
    assert result["Tue"] == ["MTH00003"]

    # Edge Case: Thời khóa biểu rỗng
    assert by_day([]) == {}


# Test 5: Module translate.py
def test_fibonacci_base_cases_and_consistency():
    """
    Test 2 hàm Fibonacci (đệ quy & vòng lặp).
    - Edge Case: Trường hợp cơ sở n = 0 và n = 1.
    - Check tính nhất quán giữa 2 thuật toán với n trong khoảng [0..10].
    """
    # Edge Case: Cơ sở n = 0, n = 1
    assert fibonacci_iterative(0) == fibonacci_recursive(0) == 0
    assert fibonacci_iterative(1) == fibonacci_recursive(1) == 1

    # Kiểm tra kết quả khớp nhau giữa đệ quy và khử đệ quy
    for n in range(2, 10):
        assert fibonacci_iterative(n) == fibonacci_recursive(n)