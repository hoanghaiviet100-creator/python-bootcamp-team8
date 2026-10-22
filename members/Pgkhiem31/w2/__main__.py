from pathlib import Path

from .io_utils import load_tasks


def main():
    project_root = Path(__file__).resolve().parents[3]
    sample_csv = project_root / "samples" / "tasks.csv"

    tasks = load_tasks(sample_csv)

    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()