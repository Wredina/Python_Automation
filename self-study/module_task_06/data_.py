# Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# � Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# � Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# � Весь период(1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# � Проверку года на високосность вынести в отдельную
# защищённую функцию
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
