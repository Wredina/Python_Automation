# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

from random import randint

print(ls := [randint(1, 7) for _ in range(20)])
# n_ls = []

print(n_ls := [i + 1 for i in range(len(ls)) if ls[i] % 2 != 0])

# for i in range(len(ls)):
#     if ls[i] % 2 != 0:
#         n_ls.append(i + 1)

# print(n_ls)
