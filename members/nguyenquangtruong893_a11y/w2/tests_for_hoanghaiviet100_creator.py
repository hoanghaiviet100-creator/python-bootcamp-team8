"""Cross-tests for hoanghaiviet100_creator's W1 modules (W2-4)."""

import pytest

from members.hoanghaiviet100_creator.w1.grades import summary
from members.hoanghaiviet100_creator.w1.rules import can_register_thesis, missing
from members.hoanghaiviet100_creator.w1.text_tools import top_k, word_count
from members.hoanghaiviet100_creator.w1.timetable import by_day
from members.hoanghaiviet100_creator.w1.translate import binary_search


def test_grades_summary_normal_and_even_odd():
    """Kiểm tra grades.summary với danh sách chẵn và lẻ phần tử."""

    assert summary([6.0, 7.5, 9.0]) == {
        "min": 6.0,
        "max": 9.0,
        "mean": 7.5,
        "median": 7.5,
    }


    assert summary([6.0, 7.5, 8.0, 9.0]) == {
        "min": 6.0,
        "max": 9.0,
        "mean": 7.62,
        "median": 7.75,
    }


def test_grades_summary_edge_case_single_and_empty():
    """Edge Case: Danh sách chỉ có 1 phần tử và ngoại lệ danh sách rỗng."""

    assert summary([8.5]) == {
        "min": 8.5,
        "max": 8.5,
        "mean": 8.5,
        "median": 8.5,
    }

    with pytest.raises(ValueError):
        summary([])




def test_rules_thesis_eligibility():
    """Kiểm tra điều kiện biên xét tốt nghiệp và các lý do thiếu."""

    assert can_register_thesis(120, 2.0) is True
    assert missing(120, 2.0) == []


    assert can_register_thesis(110, 1.8) is False
    reasons = missing(110, 1.8)
    assert any("credit" in r.lower() for r in reasons)
    assert any("gpa" in r.lower() for r in reasons)




def test_text_tools_word_count_and_top_k():
    """Kiểm tra đếm từ và sắp xếp phụ theo bảng chữ cái khi bằng tần suất."""
    text = "Git is fun. Git is fast!"
    counts = word_count(text)
    assert counts["git"] == 2
    assert counts["is"] == 2


    assert top_k(text, 2) == [("git", 2), ("is", 2)]


def test_text_tools_only_punctuation_edge_case():
    """Edge Case: Chuỗi chỉ chứa toàn ký tự dấu câu và khoảng trắng."""
    raw_text = "... ,,, !!! ??? ;: ---"
    assert word_count(raw_text) == {}
    assert top_k(raw_text, 3) == []



def test_timetable_by_day_and_empty():
    """Kiểm tra nhóm, sắp xếp mã môn theo thứ và Edge Case thời khóa biểu rỗng."""
    schedule = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]
    grouped = by_day(schedule)
    assert grouped["Mon"] == ["CSC10001", "CSC10014"]
    assert grouped["Tue"] == ["MTH00003"]

    # Edge case: Không có môn nào
    assert by_day([]) == {}




def test_binary_search_positions():
    """Kiểm tra tìm kiếm phần tử tại các vị trí đầu, giữa, cuối và không tồn tại."""
    nums = [10, 20, 30, 40, 50]
    assert binary_search(nums, 10) == 0
    assert binary_search(nums, 30) == 2
    assert binary_search(nums, 50) == 4
    assert binary_search(nums, 99) == -1


def test_binary_search_edge_cases():
    """Edge Case: Mảng rỗng, mảng 1 phần tử và mảng chứa số âm."""

    assert binary_search([], 10) == -1

   
    assert binary_search([5], 5) == 0
    assert binary_search([5], 1) == -1

    negative_nums = [-20, -10, 0, 10, 20]
    assert binary_search(negative_nums, -20) == 0
    assert binary_search(negative_nums, -10) == 1