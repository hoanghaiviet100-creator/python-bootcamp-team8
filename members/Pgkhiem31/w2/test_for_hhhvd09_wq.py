import pytest

from members.hhhvd09_wq.w1.grades import summary
from members.hhhvd09_wq.w1.rules import can_register_thesis
from members.hhhvd09_wq.w1.text_tools import top_k, word_count
from members.hhhvd09_wq.w1.timetable import by_day
from members.hhhvd09_wq.w1.translate import primes_up_to


def test_summary_empty_scores():
    with pytest.raises(ValueError):
        summary([])


def test_thesis_insufficient_credits():
    assert can_register_thesis(119, 3.0) is False


def test_primes_up_to_two():
    assert primes_up_to(2) == [2]


def test_by_day_empty():
    assert by_day([]) == {}


def test_word_count_case_insensitive():
    assert word_count("Python PYTHON python") == {"python": 3}


def test_top_k_tie_breaking():
    assert top_k("banana apple cherry", 2) == [
        ("apple", 1),
        ("banana", 1),
    ]