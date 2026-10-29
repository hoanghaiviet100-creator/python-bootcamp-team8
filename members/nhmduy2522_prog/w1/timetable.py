
def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Group courses by day of the week.

    Args:
        entries: A list of tuples containing (course, day).

    Returns:
        A dictionary mapping each day to a sorted list of course names.
    """
    result: dict[str, list[str]] = {}

    for course, day in entries:
        result.setdefault(day, []).append(course)

    for day, courses in result.items():
        courses.sort()

    return result
