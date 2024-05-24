# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.


from random import randint as rnd
from random import uniform as uni


def add_rnd_num_txt(count: int, name_file: str):
    with open(name_file, 'a', encoding='utf-8') as rnd_nums:
        for _ in range(count):
            print(rnd_nums.write(
                f'{rnd(-1000, 1000)} | {uni(-1000.0, 1000.0)}\n'))


add_rnd_num_txt(5, 'self-study\\files_sys_task_01\\rnd.txt')
