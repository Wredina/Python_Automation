# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь

########################################################################

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки.


# ВАРИАНТ 1

# def queens(location):
#     for i in range(len(location)):
#         for j in range(i+1, len(location)):
#             if i < len(location):
#                 if location[i][0] == location[j][0] or location[i][1] == location[j][1] or (location[i][0] + location[i][1]) == (location[j][0] + location[j][1]) or (location[i][0] - location[i][1]) == (location[j][0] - location[j][1]):
#                     return False
#     return True


# queens_location = [[1, 5], [2, 3], [3, 1], [4, 7], [5, 2], [6, 8], [7, 6], [8, 4]]
# print(queens(queens_location))


# ВАРИАНТ 2

# def queens(location):
#     rows = set()
#     cols = set()
#     right_diagonals = set()
#     left_diagonals = set()

#     for row, col in location:
#         if row in rows or col in cols or (row + col) in right_diagonals or (row - col) in left_diagonals:
#             return False

#         rows.add(row)
#         cols.add(col)
#         right_diagonals.add(row + col)
#         left_diagonals.add(row - col)

#     return True


# queens_location = [[1, 4], [2, 2], [3, 7], [4, 3], [5, 6], [6, 8], [7, 5], [8, 1]
#                    ]
# print(queens(queens_location))


# РЕШЕНИЕ ЗАДАЧИ 2
from random import randint as rnd


def queens(location):
    rows = set()
    cols = set()
    right_diagonals = set()
    left_diagonals = set()

    for row, col in location:
        if row in rows or col in cols or (row + col) in right_diagonals or (row - col) in left_diagonals:
            return False

        rows.add(row)
        cols.add(col)
        right_diagonals.add(row + col)
        left_diagonals.add(row - col)

    return True


max_row_col = 8
queens_location = set()

while len(queens_location) < max_row_col:
    queens_location.add((rnd(1, 8), rnd(1, 8)))
else:
    print(queens_location)
    print(queens(queens_location))
