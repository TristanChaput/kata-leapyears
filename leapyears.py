def is_leap_year(year):
    if (
        is_divisible_by(year, 100) and not is_divisible_by(year, 400)
    ) or not is_divisible_by(year, 4):
        return False
    return True


def is_divisible_by(year, number):
    return year % number == 0
