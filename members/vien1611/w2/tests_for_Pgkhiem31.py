import sys
from pathlib import Path

# Ensure repository root is on sys.path
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from members.Pgkhiem31.w1.grades import summary
from members.Pgkhiem31.w1.rules import can_register_thesis, missing
from members.Pgkhiem31.w1.text_tools import top_k, word_count
from members.Pgkhiem31.w1.timetable import by_day
from members.Pgkhiem31.w1.translate import insertion_sort


def test_grades_summary_identical_and_negative_values():
    """Edge case not in instructor tests: identical values, and negative/zero scores."""
    res_identical = summary([8.0, 8.0, 8.0, 8.0])
    assert res_identical == {"min": 8.0, "max": 8.0, "mean": 8.0, "median": 8.0}

    res_neg = summary([-4.0, 0.0, 4.0])
    assert res_neg == {"min": -4.0, "max": 4.0, "mean": 0.0, "median": 0.0}


def test_thesis_rules_boundary_cases():
    """Edge case: testing exact boundary values for credits and gpa."""
    # 1 credit short of 120
    assert not can_register_thesis(119, 2.0)
    assert missing(119, 2.0) == ["need 1 more credits"]

    # GPA just below 2.0
    assert not can_register_thesis(125, 1.8)
    assert missing(125, 1.8) == ["need GPA of 2.0, currently 1.8"]

    # Exactly meeting requirements
    assert can_register_thesis(120, 2.0)
    assert missing(120, 2.0) == []


def test_text_tools_top_k_zero_and_negative_k():
    """Edge case not in instructor tests: k <= 0 returns an empty list."""
    assert top_k("Python is awesome and versatile", 0) == []
    assert top_k("Python is awesome and versatile", -2) == []


def test_text_tools_top_k_alphabetical_tie_breaker():
    """Edge case: tie-breaking by alphabetical order when word frequencies are equal."""
    text = "zebra banana apple orange"
    result = top_k(text, 4)
    expected = [("apple", 1), ("banana", 1), ("orange", 1), ("zebra", 1)]
    assert result == expected


def test_text_tools_punctuation_only_text():
    """Edge case not in instructor tests: text containing only punctuation marks."""
    assert word_count("... !!! ??? ,,, ;;; :::") == {}


def test_timetable_reverse_sorted_entries_and_multiple_courses():
    """Edge case: multiple courses per day supplied in reverse alphabetical order."""
    data = [
        ("MATH200", "Fri"),
        ("CHEM101", "Fri"),
        ("BIO001", "Fri"),
        ("ENG102", "Tue"),
    ]
    result = by_day(data)
    assert result == {
        "Fri": ["BIO001", "CHEM101", "MATH200"],
        "Tue": ["ENG102"],
    }


def test_insertion_sort_duplicates_and_negative_numbers():
    """Edge case not in instructor tests: lists with negative numbers and duplicate elements."""
    assert insertion_sort([5, -2, 3, -2, 0, 8, 3]) == [-2, -2, 0, 3, 3, 5, 8]
    assert insertion_sort([42]) == [42]
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
