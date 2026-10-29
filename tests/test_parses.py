
from datetime import date

import pytest

from shared.study_planner.parses import parse_csv


def test_parse_csv_success(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,2026-10-30\n"
        "Assignment,4,1.5,2026-10-27\n",
        encoding="utf-8",
    )

    tasks = parse_csv(str(csv_file))

    assert len(tasks) == 2
    assert tasks[0].title == "DS exam"
    assert tasks[0].importance == 5
    assert tasks[0].effort_h == 6.0
    assert tasks[0].deadline == date(2026, 10, 30)


def test_parse_csv_invalid_effort(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,invalid_effort,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="row 2"):
        parse_csv(str(csv_file))


def test_parse_csv_missing_column(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,deadline\n"
        "DS exam,5,2026-10-30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="effort_h"):
        parse_csv(str(csv_file))


def test_parse_csv_empty_file(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="header"):
        parse_csv(str(csv_file))


def test_parse_csv_invalid_deadline(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,30-10-2026\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="row 2"):
        parse_csv(str(csv_file))
