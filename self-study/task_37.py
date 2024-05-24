# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
import os


def func(us_str):
    *path_lst, file = os.path.split(us_str)
    path = os.path.join(*path_lst)
    name, exp = file.split('.')
    return (path, name, exp)


txt = 'D:\программирование\Обучение_тестировщик\Python\self-study\\task_37.py'


print(func(txt))
