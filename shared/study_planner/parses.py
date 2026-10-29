
import csv
from datetime import datetime
from pathlib import Path

from shared.contract import Task
from shared.study_planner.validate import validate_tasks


def parse_csv(path: str) -> list[Task]:
    """Read tasks from a CSV file and validate the parsed data.

    Args:
        path: Path to the input CSV file.

    Returns:
        A list of validated Task objects.

    Raises:
        ValueError: If the CSV format or task data is invalid.
        FileNotFoundError: If the file does not exist.
    """
    tasks: list[Task] = []
    required_columns = {"title", "importance", "effort_h", "deadline"}

    with Path(path).open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty or missing its header.")

        missing_columns = required_columns - set(reader.fieldnames)
        if missing_columns:
            columns = ", ".join(sorted(missing_columns))
            raise ValueError(f"CSV is missing required columns: {columns}.")

        for row_number, row in enumerate(reader, start=2):
            try:
                title = (row.get("title") or "").strip()
                importance_text = (row.get("importance") or "").strip()
                effort_text = (row.get("effort_h") or "").strip()
                deadline_text = (row.get("deadline") or "").strip()

                if not title:
                    raise ValueError("title must not be empty.")

                if not importance_text:
                    raise ValueError("importance must not be empty.")

                if not effort_text:
                    raise ValueError("effort_h must not be empty.")

                if not deadline_text:
                    raise ValueError("deadline must not be empty.")

                task = Task(
                    title=title,
                    importance=int(importance_text),
                    effort_h=float(effort_text),
                    deadline=datetime.strptime(
                        deadline_text, "%Y-%m-%d"
                    ).date(),
                )
            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Invalid data on CSV row {row_number}: {error}"
                ) from error

            tasks.append(task)

    validate_tasks(tasks)
    return tasks
