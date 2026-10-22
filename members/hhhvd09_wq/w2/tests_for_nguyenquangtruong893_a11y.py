
import pytest

from members.nguyenquangtruong893_a11y.w1.grades import summary
from members.nguyenquangtruong893_a11y.w1.rules import can_register_thesis
from members.nguyenquangtruong893_a11y.w1.text_tools import top_k, word_count
from members.nguyenquangtruong893_a11y.w1.timetable import by_day
from members.nguyenquangtruong893_a11y.w1.translate import is_palindrome


def test_summary_empty_scores():
    with pytest.raises(ValueError):
        summary([])


def test_thesis_insufficient_credits():
    assert can_register_thesis(119, 3.0) is False


def test_palindrome_basic():
    assert is_palindrome("racecar") is True
    assert is_palindrome("python") is False


def test_by_day_empty():
    assert by_day([]) == {}


def test_word_count_case_insensitive():
    assert word_count("Python PYTHON python") == {"python": 3}


def test_top_k_tie_breaking():
    assert top_k("banana apple cherry", 2) == [
        ("apple", 1),
        ("banana", 1),
    ]
