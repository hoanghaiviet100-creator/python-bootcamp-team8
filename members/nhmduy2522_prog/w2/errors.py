from .models import (
    Task,  # Hoặc "from models import Task" tùy cách tổ chức import của dự án
)


class InfeasiblePlan(Exception):
    """Ngoại lệ xảy ra khi tổng số giờ thực hiện các công việc vượt quá số giờ khả dụng."""

    def __init__(self, needed_h: float, available_h: float):
        super().__init__()
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        return (
            f"Infeasible plan: needed {self.needed_h} hours, "
            f"but only {self.available_h} hours available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Kiểm tra xem kế hoạch có khả thi hay không.

    Tính tổng số giờ cần thiết từ thuộc tính `effort_h` của danh sách task.
    Nếu vượt quá `available_h`, quăng ngoại lệ `InfeasiblePlan`.
    """
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)