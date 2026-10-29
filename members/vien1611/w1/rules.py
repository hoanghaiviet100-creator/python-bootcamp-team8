def can_register_thesis(credits: int, gpa: float) -> bool:
    return bool(credits >= 120 and gpa >= 2.0)

def missing(credits: int, gpa: float) -> list[str]:
    result = []
    if credits < 120:
        missing_credits = 120 - credits
        result.append(f"need {missing_credits} more credits")
    if gpa < 2.0:
        missing_gpa = 2.0 - gpa
        result.append(f"need {round(missing_gpa, 2)} more gpa")
    return result

print(can_register_thesis(118, 2.5)) 
print(missing(118, 1.5))           