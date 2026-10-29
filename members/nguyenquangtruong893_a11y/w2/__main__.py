"""Entry point for running w2 as a module."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:

    repo_root = Path(__file__).resolve().parents[3]
    sample_csv = repo_root / "samples" / "tasks.csv"

    if not sample_csv.exists():
        sample_csv = Path("samples/tasks.csv")
    if not sample_csv.exists():
        sample_csv = Path("python-bootcamp/samples/tasks.csv")

    if not sample_csv.exists():
        print(f"Error: Sample file not found at {sample_csv}")
        return

    tasks = load_tasks(sample_csv)
    print(f"Loaded {len(tasks)} tasks from {sample_csv.name}:")
    for idx, task in enumerate(tasks, start=1):
        print(
            f"{idx}. {task.title} | Importance: {task.importance} | "
            f"Effort: {task.effort_h}h | Deadline: {task.deadline}"
        )


if __name__ == "__main__":
    main()
