def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"cần thêm {needed_credits} tín chỉ")
    if gpa < 2.0:
        reasons.append(f"GPA chưa đạt 2.0 (hiện tại là {gpa})")
    return reasons