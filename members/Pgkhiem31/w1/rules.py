#rules.py
def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    result = []

    if credits < 120:
        result.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        result.append(f"need GPA of 2.0, currently {gpa}")

    return result