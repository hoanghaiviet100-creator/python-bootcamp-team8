"""T-W3 Member 2: test the team CLI with real CSV files and subprocesses.

Run from the repository root:
    python -m pytest -v shared/study_planner/test_study_planner_e2e.py

These tests require Member 1's shared/study_planner/__main__.py and the
team's parse_csv, prioritise, allocate, and render implementations. Missing
integration is reported as a failure, rather than skipped or mocked.
"""

import csv
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run_planner(csv_path: Path, hours: float) -> subprocess.CompletedProcess[str]:
    """Run the public team CLI in a fresh Python process from the project root."""
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "shared.study_planner",
            str(csv_path),
            "--hours",
            str(hours),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )


def assert_task_hours(output: str, title: str, hours: float) -> None:
    """Check rendered task hours without depending on padding or numbering."""
    matches = re.findall(
        re.escape(title) + r"[^\r\n]*?([0-9]+(?:\.[0-9]+)?)\s*h\b",
        output,
        flags=re.IGNORECASE,
    )
    assert len(matches) == 1, f"Expected one plan entry for {title!r}:\n{output}"
    assert float(matches[0]) == hours, output


def test_team_cli_with_repository_sample() -> None:
    """Load the repository sample and render both tasks with a feasible budget."""
    result = run_planner(ROOT / "samples" / "tasks.csv", hours=7.5)

    assert result.returncode == 0, (
        f"Team CLI exited with {result.returncode}.\n"
        f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )
    assert_task_hours(result.stdout, "DS exam", 6.0)
    assert_task_hours(result.stdout, "Assignment", 1.5)


def test_team_cli_prioritises_csv_tasks(tmp_path: Path) -> None:
    """Prioritise by urgency rather than CSV order, independent of today's date."""
    today = date.today()
    csv_path = tmp_path / "sample study tasks.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["title", "importance", "effort_h", "deadline"])
        writer.writerow(["DS exam", 5, 1.0, (today + timedelta(days=4)).isoformat()])
        writer.writerow(["Assignment", 4, 1.5, (today + timedelta(days=1)).isoformat()])

    result = run_planner(csv_path, hours=2.5)

    assert result.returncode == 0, (
        f"Team CLI exited with {result.returncode}.\n"
        f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
    )
    assert_task_hours(result.stdout, "Assignment", 1.5)
    assert_task_hours(result.stdout, "DS exam", 1.0)
    assert result.stdout.index("Assignment") < result.stdout.index(
        "DS exam"
    ), result.stdout
