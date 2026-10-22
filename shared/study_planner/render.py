"""Render allocated study blocks as a readable study plan."""

from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Convert study blocks into a formatted string."""
    lines = ["Study Plan"]

    if not blocks:
        lines.append("No study blocks.")
    else:
        for index, block in enumerate(blocks, start=1):
            lines.append(
                f"{index}. {block.task.title} - {block.hours:.1f} h"
            )

    total_hours = sum(block.hours for block in blocks)
    lines.append(f"Total: {total_hours:.1f} h")

    return "\n".join(lines)