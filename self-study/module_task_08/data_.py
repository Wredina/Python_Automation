# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку

from random import randint as rnd


def real_data(data: str) -> bool:
    day, mount, year = list(map(int, (data.split('.'))))
    if 0 < year < 10000:
        if 0 < mount < 12:
            if mount == 4 or mount == 6 or mount == 9 or mount == 11:
                if 0 < day < 32:
                    return True
            elif mount == 2:
                if _leap_year(year):
                    if 0 < day < 30:
                        return True
                else:
                    if 0 < day < 29:
                        return True
            else:
                if 0 < day < 31:
                    return True
    return False


def _leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False
