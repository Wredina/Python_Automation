# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами(3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
from random import randint


def company(dct: dict) -> bool:
    # for i in dct:
    #     dct[i] = sum(dct[i])
    # return all(map(lambda x: x > 0, dct.values()))
    for i in dct.values():
        if sum(i) < 0:
            return False
    return True


companies = {name: [randint(-100000, 100000)
                    for _ in range(randint(3, 10))] for name in ['comp1', 'comp2', 'comp3', 'comp4']}

print(company(companies))
