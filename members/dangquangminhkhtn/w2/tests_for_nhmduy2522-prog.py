import pytest

from members.nhmduy2522_prog.w1.grades import summary
from members.nhmduy2522_prog.w1.rules import word_count as rules_word_count
from members.nhmduy2522_prog.w1.rules import top_k as rules_top_k
from members.nhmduy2522_prog.w1.text_tools import word_count as tools_word_count
from members.nhmduy2522_prog.w1.text_tools import top_k as tools_top_k
from members.nhmduy2522_prog.w1.timetable import by_day
from members.nhmduy2522_prog.w1.translate import bubble_sort


def test_summary_normal():
    assert summary([7.5, 9, 6, 8]) == {
        "min": 6,
        "max": 9,
        "mean": 7.63,
        "median": 7.75,
    }


def test_summary_single_score():
    assert summary([8]) == {
        "min": 8,
        "max": 8,
        "mean": 8,
        "median": 8,
    }


def test_summary_empty_list():
    with pytest.raises(ValueError):
        summary([])


def test_rules_word_count():
    assert rules_word_count("Git is fun. Git is fast!") == {
        "git": 2,
        "is": 2,
        "fun": 1,
        "fast": 1,
    }


def test_rules_top_k_tie_breaking():
    assert rules_top_k("banana apple banana apple", 2) == [
        ("apple", 2),
        ("banana", 2),
    ]


def test_text_tools_word_count():
    assert tools_word_count("Hello, HELLO! World.") == {
        "hello": 2,
        "world": 1,
    }


def test_text_tools_top_k_zero():
    assert tools_top_k("apple banana apple", 0) == []


def test_by_day_normal():
    assert by_day([
        ("Math", "Monday"),
        ("Physics", "Tuesday"),
        ("Biology", "Monday"),
    ]) == {
        "Monday": ["Biology", "Math"],
        "Tuesday": ["Physics"],
    }


def test_by_day_empty():
    assert by_day([]) == {}


def test_bubble_sort_normal():
    assert bubble_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_duplicates_and_negative_numbers():
    assert bubble_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]