
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.
from random import randint

ls = (1, 'text', [1, 2], 'text2', 12, True, None, [3, 5], 13, False)

dt = {}

for i in ls:  # проходимся по кортежу
    if type(i) in dt:  # если есть этот тип в словаре
        # добавляем значение в список значений этого типа
        dt[type(i)].append(i)
    else:  # если этого типа нет
        dt[type(i)] = [i]  # добавляем пару ключь-значение

print(dt)
