# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между  переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
from random import randint


def func(lst: list[int], low: int, up: int) -> int:
    if low < 0:
        low = len(lst) - -low
    if up < 0:
        up = len(lst) - -up

    low, up = sorted([low, up])
    return sum(lst[low:up+1])


numbers = [randint(1, 15) for i in range(15)]
indx_low = randint(-5, 15)
indx_up = randint(-5, 15)
print(numbers)
print(indx_low, indx_up)


print(func(numbers, indx_low, indx_up))
