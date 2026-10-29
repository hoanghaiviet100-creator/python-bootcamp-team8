"""Check thesis registration requirements and explain unmet criteria."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether the student has at least 120 credits and a 2.0 GPA."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List the credit and GPA requirements the student has not met."""
    result: list[str] = []

    if credits < 120:
        result.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        result.append(f"need GPA of 2.0, currently {gpa}")

    return result
