from pathlib import Path

from .io_utils import load_tasks


def main():
    repo_root = Path(__file__).resolve().parents[3]
    sample_csv = repo_root / "samples" / "tasks.csv"
    if not sample_csv.exists():
        sample_csv = Path("samples/tasks.csv")
    tasks = load_tasks(sample_csv)
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()
