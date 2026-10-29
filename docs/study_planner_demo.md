# Study Planner – T-W3 Demo

## Input

Run the demonstration from the repository root using `samples/tasks.csv`:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

## Command

Run this **after** the team has integrated `shared/study_planner/__main__.py`:

```cmd
python -m shared.study_planner samples/tasks.csv --hours 2
```

## Expected workflow

The CLI reads the CSV, prioritises tasks, allocates 2 hours and prints the result using `render()`.

For a planning date of 2026-10-26, the existing `prioritise()` and `allocate()` implementations would yield:

```text
Study Plan
1. Assignment - 1.5 h
2. DS exam - 0.5 h
Total: 2.0 h
```

This is a calculated example, **not an observed run of the unfinished integrated CLI**. As the shared CLI currently has no `--today` option in the stated task, its result can vary according to the actual date.

## Verification after integration

1. Confirm the CLI runs from a fresh clone.
2. Check a missing CSV path produces a clear error.
3. Check an empty input file is handled explicitly.
4. Check an infeasible plan is reported according to the team's agreed behavior.
5. Run the end-to-end pytest test and Ruff; record the actual results in the PR.
