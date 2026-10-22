"""Module for exporting study plans to different formats (JSON, Markdown)."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any, Sequence, Union

from shared.contract import Block, Task

PlanItem = Union[Block, Task]


def _item_to_dict(item: PlanItem) -> dict[str, Any]:
    """Convert a Block or Task item into a standardized dictionary."""
    if isinstance(item, Block):
        task = item.task
        allocated_hours = float(item.hours)
    elif isinstance(item, Task):
        task = item
        allocated_hours = float(item.effort_h)
    elif hasattr(item, "task") and hasattr(item, "hours"):
        task = item.task
        allocated_hours = float(item.hours)
    else:
        task = item
        allocated_hours = float(getattr(item, "effort_h", getattr(item, "hours", 0.0)))

    deadline_val = getattr(task, "deadline", None)
    if isinstance(deadline_val, date):
        deadline_str = deadline_val.isoformat()
    elif hasattr(deadline_val, "isoformat"):
        deadline_str = deadline_val.isoformat()
    else:
        deadline_str = str(deadline_val)

    return {
        "title": getattr(task, "title", ""),
        "importance": int(getattr(task, "importance", 1)),
        "effort_h": float(getattr(task, "effort_h", 0.0)),
        "deadline": deadline_str,
        "hours": allocated_hours,
        "allocated_hours": allocated_hours,
    }


def export_json(
    plan: Sequence[PlanItem],
    path: str | Path,
    *,
    indent: int = 2,
    include_summary: bool = False,
) -> Path:
    """Export the study plan to a JSON file.

    Parameters
    ----------
    plan : Sequence[Block | Task]
        A sequence of Block or Task objects representing the study plan.
    path : str | Path
        Target file path for the JSON file.
    indent : int, default 2
        Indentation spaces for JSON formatting.
    include_summary : bool, default False
        If True, outputs an object with metadata and a list of blocks.

    Returns
    -------
    Path
        The Path object of the saved JSON file.
    """
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    items_data = [_item_to_dict(item) for item in plan]

    if include_summary:
        total_hours = sum(entry["allocated_hours"] for entry in items_data)
        data: Any = {
            "total_tasks": len(items_data),
            "total_allocated_hours": total_hours,
            "blocks": items_data,
        }
    else:
        data = items_data

    with open(out_path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

    return out_path


def export_markdown(
    plan: Sequence[PlanItem],
    path: str | Path | None = None,
    *,
    title: str = "Study Plan Report",
) -> str:
    """Export the study plan to a Markdown formatted report.

    Parameters
    ----------
    plan : Sequence[Block | Task]
        A sequence of Block or Task objects representing the study plan.
    path : str | Path | None, optional
        Target file path. If None, the report is generated without saving to disk.
    title : str, default 'Study Plan Report'
        Header title for the Markdown document.

    Returns
    -------
    str
        The Markdown report content.
    """
    items_data = [_item_to_dict(item) for item in plan]
    total_tasks = len(items_data)
    total_allocated = sum(item["allocated_hours"] for item in items_data)
    total_effort = sum(item["effort_h"] for item in items_data)

    lines: list[str] = [f"# {title}", ""]

    if not items_data:
        lines.append("*No study blocks scheduled.*")
        lines.append("")
    else:
        lines.append("## Summary")
        lines.append(f"- **Total Tasks**: {total_tasks}")
        lines.append(f"- **Total Allocated Hours**: {total_allocated:.1f} h")
        lines.append(f"- **Total Estimated Effort**: {total_effort:.1f} h")
        lines.append("")
        lines.append("## Schedule")
        lines.append("| # | Title | Importance | Effort (h) | Allocated (h) | Deadline |")
        lines.append("|---|---|---|---|---|---|")
        for idx, item in enumerate(items_data, start=1):
            lines.append(
                f"| {idx} | {item['title']} | {item['importance']} | "
                f"{item['effort_h']:.1f} | {item['allocated_hours']:.1f} | {item['deadline']} |"
            )
        lines.append("")

    content = "\n".join(lines)

    if path is not None:
        out_path = Path(path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, mode="w", encoding="utf-8") as f:
            f.write(content)

    return content


def export_plan(
    plan: Sequence[PlanItem],
    path: str | Path,
    *,
    format: str | None = None,
) -> Path:
    """Export the study plan to a file, detecting or using the specified format.

    Parameters
    ----------
    plan : Sequence[Block | Task]
        A sequence of Block or Task objects representing the study plan.
    path : str | Path
        Target file path.
    format : str | None, optional
        Format identifier ('json', 'markdown', 'md'). If None, inferred from path suffix.

    Returns
    -------
    Path
        The Path object of the saved file.

    Raises
    ------
    ValueError
        If the format is unrecognized or cannot be inferred from extension.
    """
    out_path = Path(path)
    fmt = format.lower() if format is not None else None

    if fmt is None:
        ext = out_path.suffix.lower()
        if ext == ".json":
            fmt = "json"
        elif ext in {".md", ".markdown"}:
            fmt = "markdown"
        else:
            raise ValueError(
                f"Cannot infer format from file extension '{ext}'. "
                "Please specify format='json' or format='markdown'."
            )

    if fmt == "json":
        export_json(plan, out_path)
    elif fmt in {"markdown", "md"}:
        export_markdown(plan, out_path)
    else:
        raise ValueError(
            f"Unsupported format: '{format}'. Supported formats are 'json' and 'markdown'."
        )

    return out_path
