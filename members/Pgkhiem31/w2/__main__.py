"""Print the repository sample tasks when the Week 2 package is executed."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load samples/tasks.csv relative to the project and print each task."""
    project_root = Path(__file__).resolve().parents[3]
    sample_csv = project_root / "samples" / "tasks.csv"

    tasks = load_tasks(sample_csv)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()
