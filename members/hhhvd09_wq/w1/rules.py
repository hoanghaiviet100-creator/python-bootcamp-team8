def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether the credit and GPA requirements are met."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List unmet thesis eligibility requirements."""
    reasons = []

    if credits < 120:
        needed = 120 - credits
        reasons.append(f"need {needed} more credits")

    if gpa < 2.0:
        reasons.append("need GPA of at least 2.0")

    return reasons
