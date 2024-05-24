# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».
from random import randint


def func(n):
    for i in range(1, n):
        for j in range(2, n):
            if i > j:
                if i % j == 0:
                    break
                elif j == n - 1:
                    yield i
            elif i == j:
                yield i


num = func(randint(50, 500))
for i in num:
    print(i)
