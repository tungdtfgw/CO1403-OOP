def add(a, b):
    c = a + b
    return c


# 0 - dưới 40: failed
# 40 - dưới 60: passed
# 60 - dưới 80: merit
# 80 - 100: distinction
# < 0 hoặc > 100: invalid
def rank(grade):
    if grade < 0 or grade > 100:
        return "invalid"
    elif grade < 40:
        return "failed"
    elif grade < 60:
        return "passed"
    elif grade < 80:
        return "merit"
    else:
        return "distinction"