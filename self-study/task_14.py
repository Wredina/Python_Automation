# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

from random import randint

ls = sorted([randint(1, 5) for _ in range(20)])
# ls = sorted([2, 4, 3, 3, 2, 3, 4, 3, 1, 4, 5, 3, 2, 3, 1])
print(ls)

n_ls = [ls.index]

for i in ls:
    if ls.count(i) % 2 == 0:
        for _ in range(ls.count(i)):
            ls.remove(i)
    elif ls.count(i) % 2 != 0:
        for _ in range(ls.count(i) - 1):
            ls.remove(i)

print(ls)
