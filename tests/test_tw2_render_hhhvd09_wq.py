"""Unit tests for the T-W2 study plan renderer."""

from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def make_block(title: str, hours: float) -> Block:
    task = Task(
        title=title,
        importance=3,
        effort_h=5.0,
        deadline=date(2026, 10, 30),
    )
    return Block(task=task, hours=hours)


def test_empty_blocks():
    result = render([])

    assert result == (
        "Study Plan\n"
        "No study blocks.\n"
        "Total: 0.0 h"
    )


def test_single_block():
    result = render([make_block("Assignment", 1.5)])

    assert "1. Assignment - 1.5 h" in result
    assert "Total: 1.5 h" in result


def test_multiple_blocks():
    blocks = [
        make_block("Assignment", 1.5),
        make_block("DS exam", 0.5),
    ]

    result = render(blocks)

    assert "1. Assignment - 1.5 h" in result
    assert "2. DS exam - 0.5 h" in result
    assert "Total: 2.0 h" in result


def test_uses_allocated_hours():
    block = make_block("DS exam", 0.5)

    result = render([block])

    assert "DS exam - 0.5 h" in result
    assert "Total: 0.5 h" in result


def test_preserves_order():
    blocks = [
        make_block("First", 1.0),
        make_block("Second", 2.0),
    ]

    result = render(blocks)

    assert result.index("First") < result.index("Second")


def test_does_not_modify_input():
    blocks = [
        make_block("Math", 1.0),
        make_block("Python", 2.0),
    ]

    original = blocks.copy()

    render(blocks)

    assert blocks == original