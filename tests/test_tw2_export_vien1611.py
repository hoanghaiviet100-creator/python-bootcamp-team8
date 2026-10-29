"""Unit tests for the T-W2 study plan export module."""

import json
from datetime import date
from pathlib import Path

import pytest

from shared.contract import Block, Task
from shared.study_planner.export import (
    export_json,
    export_markdown,
    export_plan,
)


def make_block(title: str, hours: float, importance: int = 3, effort_h: float = 4.0) -> Block:
    task = Task(
        title=title,
        importance=importance,
        effort_h=effort_h,
        deadline=date(2026, 10, 30),
    )
    return Block(task=task, hours=hours)


def test_export_json_blocks(tmp_path: Path):
    blocks = [
        make_block("DS exam", 2.5, importance=5, effort_h=6.0),
        make_block("Assignment", 1.5, importance=4, effort_h=2.0),
    ]
    out_file = tmp_path / "plan.json"
    result_path = export_json(blocks, out_file)

    assert result_path == out_file
    assert out_file.exists()

    data = json.loads(out_file.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert data[0]["title"] == "DS exam"
    assert data[0]["importance"] == 5
    assert data[0]["effort_h"] == 6.0
    assert data[0]["deadline"] == "2026-10-30"
    assert data[0]["hours"] == 2.5
    assert data[0]["allocated_hours"] == 2.5


def test_export_json_tasks(tmp_path: Path):
    tasks = [
        Task(title="Reading", importance=2, effort_h=3.0, deadline=date(2026, 11, 1)),
    ]
    out_file = tmp_path / "tasks.json"
    export_json(tasks, out_file)

    data = json.loads(out_file.read_text(encoding="utf-8"))
    assert len(data) == 1
    assert data[0]["title"] == "Reading"
    assert data[0]["allocated_hours"] == 3.0


def test_export_json_with_summary(tmp_path: Path):
    blocks = [
        make_block("Task A", 2.0, effort_h=3.0),
        make_block("Task B", 1.5, effort_h=2.0),
    ]
    out_file = tmp_path / "summary.json"
    export_json(blocks, out_file, include_summary=True)

    data = json.loads(out_file.read_text(encoding="utf-8"))
    assert data["total_tasks"] == 2
    assert data["total_allocated_hours"] == 3.5
    assert len(data["blocks"]) == 2


def test_export_json_empty(tmp_path: Path):
    out_file = tmp_path / "empty.json"
    export_json([], out_file)
    assert json.loads(out_file.read_text(encoding="utf-8")) == []


def test_export_markdown_file_and_return_value(tmp_path: Path):
    blocks = [
        make_block("DS exam", 2.0, importance=5, effort_h=5.0),
        make_block("Assignment", 1.0, importance=4, effort_h=2.0),
    ]
    out_file = tmp_path / "report.md"
    content = export_markdown(blocks, out_file, title="Weekly Review")

    assert out_file.exists()
    file_content = out_file.read_text(encoding="utf-8")
    assert content == file_content

    assert "# Weekly Review" in content
    assert "- **Total Tasks**: 2" in content
    assert "- **Total Allocated Hours**: 3.0 h" in content
    assert "- **Total Estimated Effort**: 7.0 h" in content
    assert "| 1 | DS exam | 5 | 5.0 | 2.0 | 2026-10-30 |" in content
    assert "| 2 | Assignment | 4 | 2.0 | 1.0 | 2026-10-30 |" in content


def test_export_markdown_in_memory():
    blocks = [make_block("Quick task", 1.0)]
    content = export_markdown(blocks, path=None)
    assert "# Study Plan Report" in content
    assert "Quick task" in content


def test_export_markdown_empty():
    content = export_markdown([])
    assert "*No study blocks scheduled.*" in content


def test_export_plan_auto_detect(tmp_path: Path):
    blocks = [make_block("Math", 2.0)]

    json_path = tmp_path / "plan.json"
    export_plan(blocks, json_path)
    assert json_path.exists()
    assert json.loads(json_path.read_text(encoding="utf-8"))[0]["title"] == "Math"

    md_path = tmp_path / "plan.md"
    export_plan(blocks, md_path)
    assert md_path.exists()
    assert "Math" in md_path.read_text(encoding="utf-8")


def test_export_plan_explicit_format(tmp_path: Path):
    blocks = [make_block("Physics", 3.0)]

    # File without extension but explicit format
    custom_path = tmp_path / "output_file"
    export_plan(blocks, custom_path, format="json")
    assert json.loads(custom_path.read_text(encoding="utf-8"))[0]["title"] == "Physics"


def test_export_plan_invalid_format(tmp_path: Path):
    blocks = [make_block("Physics", 3.0)]

    # Unknown extension
    with pytest.raises(ValueError, match="Cannot infer format"):
        export_plan(blocks, tmp_path / "plan.xyz")

    # Unsupported explicit format
    with pytest.raises(ValueError, match="Unsupported format"):
        export_plan(blocks, tmp_path / "plan.json", format="xml")


def test_export_unicode_support(tmp_path: Path):
    blocks = [
        make_block("Ôn thi Giải tích", 3.0, importance=5, effort_h=4.0),
        make_block("Bài tập lớn Lập trình", 2.5, importance=4, effort_h=5.0),
    ]
    json_path = tmp_path / "vietnamese.json"
    export_json(blocks, json_path)
    content_json = json_path.read_text(encoding="utf-8")
    assert "Ôn thi Giải tích" in content_json

    md_path = tmp_path / "vietnamese.md"
    export_markdown(blocks, md_path)
    content_md = md_path.read_text(encoding="utf-8")
    assert "Bài tập lớn Lập trình" in content_md


def test_export_creates_parent_directories(tmp_path: Path):
    nested_file = tmp_path / "deep" / "nested" / "folder" / "plan.json"
    assert not nested_file.parent.exists()

    export_json([make_block("Nested", 1.0)], nested_file)
    assert nested_file.exists()
