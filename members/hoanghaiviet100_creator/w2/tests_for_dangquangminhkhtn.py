
import pytest

from members.dangquangminhkhtn.w1.grades import summary
from members.dangquangminhkhtn.w1.rules import can_register_thesis, missing
from members.dangquangminhkhtn.w1.text_tools import top_k, word_count
from members.dangquangminhkhtn.w1.timetable import by_day
from members.dangquangminhkhtn.w1.translate import transpose

# ===== grades.py =====

def test_summary_normal():
    assert summary([6.0, 8.0, 10.0]) == {
        "min": 6.0,
        "max": 10.0,
        "mean": 8.0,
        "median": 8.0
    }


def test_summary_empty():
    with pytest.raises(ValueError, match="scores must not be empty"):
        summary([])


# ===== rules.py =====

def test_can_register_thesis():
    assert can_register_thesis(120, 2.0) is True
    assert can_register_thesis(119, 3.5) is False
    assert can_register_thesis(130, 1.9) is False


def test_missing_both_conditions():
    assert missing(115, 1.5) == [
        "need 5 more credits",
        "need 0.50 more gpa"
    ]


# ===== text_tools.py =====

def test_word_count():
    assert word_count("Hello, hello! Python.") == {
        "hello": 2,
        "python": 1
    }


def test_top_k_tie_breaking():
    # Edge case: equal frequencies must be sorted alphabetically
    assert top_k("banana apple cherry", 2) == [
        ("apple", 1),
        ("banana", 1)
    ]


# ===== timetable.py =====

def test_by_day():
    assert by_day([
        ("Math", "Monday"),
        ("Physics", "Monday"),
        ("English", "Tuesday")
    ]) == {
        "Monday": ["Math", "Physics"],
        "Tuesday": ["English"]
    }


# ===== translate.py =====

def test_transpose_rectangular_matrix():
    assert transpose([
        [1, 2, 3],
        [4, 5, 6]
    ]) == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_transpose_empty_matrix():
    # Edge case: empty matrix
    assert transpose([]) == []
