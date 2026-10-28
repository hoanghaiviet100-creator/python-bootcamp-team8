# Study Planner – Team 8

## Overview

The Study Planner reads tasks from CSV, prioritises tasks, allocates study hours, and renders a text plan. This is the team's CSC10014 Python Bootcamp T-W3 integration project.

## Requirements

Run the application with Python 3.12 from the repository root after the T-W3 CLI is integrated.

## Input CSV

The `samples/tasks.csv` file has the columns `title,importance,effort_h,deadline`.

- `title`: Task name
- `importance`: Integer from 1 to 5
- `effort_h`: Estimated number of hours
- `deadline`: ISO date (`YYYY-MM-DD`)

## Components

- `shared/contract.py`: `Task` and `Block` dataclasses
- `shared/study_planner/parses.py`: `parse_csv()` loads CSV tasks
- `shared/study_planner/prioritise.py`: `prioritise()` orders tasks by urgency
- `shared/study_planner/allocate.py`: `allocate()` assigns available hours
- `shared/study_planner/render.py`: `render()` formats the study plan
- `shared/study_planner/__main__.py`: team CLI integration (T-W3)

## Run

Once the team has merged `__main__.py`:

```cmd
python -m shared.study_planner samples/tasks.csv --hours 2
```

The CLI should call `parse_csv` → `prioritise` → `allocate` → `render`.

## Test and lint

```cmd
python -m pytest -q
python -m ruff check shared
```

The team must test missing and empty files and infeasible plans. The end-to-end test and CLI must pass from a fresh clone before T-W3 is complete.

See `docs/study_planner_demo.md` for a walkthrough.
