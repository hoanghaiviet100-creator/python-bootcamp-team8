import argparse
import sys
from datetime import date
from pathlib import Path

from members.hoanghaiviet100_creator.w2.errors import InfeasiblePlan
from shared.study_planner.allocate import allocate
from shared.study_planner.parses import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main() -> None:
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    parser.add_argument("csv_file", type=Path, help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument(
        "--today",
        type=str,
        default=str(date.today()),
        help="Date in YYYY-MM-DD format",
    )

    args = parser.parse_args()

    # 1. Báo lỗi nếu file không tồn tại (Xử lý lỗi Member 3)
    if not args.csv_file.exists():
        sys.stderr.write(f"Error: File '{args.csv_file}' not found.\n")
        sys.exit(1)

    try:
        today_date = date.fromisoformat(args.today)

        # Step 1: Parse CSV
        tasks = parse_csv(str(args.csv_file))

        # 2. Báo lỗi nếu file rỗng (Xử lý lỗi Member 3)
        if not tasks:
            sys.stderr.write("Error: Tasks file is empty.\n")
            sys.exit(1)

        # Step 2: Prioritise
        prioritised_tasks = prioritise(tasks, today=today_date)

        # Step 3: Allocate
        blocks = allocate(prioritised_tasks, hours=args.hours)

        # 3. Báo lỗi nếu kế hoạch không khả thi (Xử lý lỗi Member 3)
        if args.hours <= 0 or (tasks and not blocks):
            raise InfeasiblePlan("Not enough available hours to allocate any task.")

        # Step 4: Render
        output = render(blocks)
        print(output)

    except InfeasiblePlan as err:
        sys.stderr.write(f"Error: Infeasible plan - {err}\n")
        sys.exit(1)
    except Exception as err:
        sys.stderr.write(f"Error: {err}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()