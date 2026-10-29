from pathlib import Path

from members.nhmduy2522_prog.w2.io_utils import load_tasks

CSV_PATH = Path(__file__).parent / "tasks.csv"

if __name__ == "__main__":
    tasks = load_tasks(CSV_PATH)
    for task in tasks:
        print(task)