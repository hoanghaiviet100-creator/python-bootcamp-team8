from datetime import date
from shared.contract import Task


def validate_tasks(tasks: list[Task]) -> bool:
    """Kiểm tra tính hợp lệ của danh sách các Task.

    - Kiểm tra danh sách rỗng / tiêu đề trống
    - Phát hiện task trùng lặp tiêu đề
    - Kiểm tra tầm quan trọng (importance) từ 1-5
    - Kiểm tra thời gian (effort_h) phải > 0
    - Kiểm tra kiểu dữ liệu của deadline
    """
    if not tasks:
        raise ValueError("Danh sách task không được rỗng.")

    seen_titles = set()

    for idx, task in enumerate(tasks, start=1):
        # 1. Kiểm tra tiêu đề bị trống/rỗng
        if not task.title or not task.title.strip():
            raise ValueError(f"Task #{idx}: Tiêu đề (title) không được để rỗng.")

        # 2. Kiểm tra trùng lặp tiêu đề (không phân biệt hoa/thường)
        clean_title = task.title.strip().lower()
        if clean_title in seen_titles:
            raise ValueError(
                f"Task #{idx}: Phát hiện trùng lặp tiêu đề '{task.title}'."
            )
        seen_titles.add(clean_title)

        # 3. Kiểm tra importance thuộc khoảng 1-5
        if not (1 <= task.importance <= 5):
            raise ValueError(
                f"Task #{idx} ('{task.title}'): importance phải từ 1 đến 5 (giá trị: {task.importance})."
            )

        # 4. Kiểm tra effort_h phải > 0
        if task.effort_h <= 0:
            raise ValueError(
                f"Task #{idx} ('{task.title}'): effort_h phải lớn hơn 0 (giá trị: {task.effort_h})."
            )

        # 5. Kiểm tra deadline đúng kiểu datetime.date
        if not isinstance(task.deadline, date):
            raise ValueError(
                f"Task #{idx} ('{task.title}'): deadline phải là kiểu datetime.date."
            )

    return True