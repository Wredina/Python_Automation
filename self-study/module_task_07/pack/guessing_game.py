# Улучшаем задачу module_task_01
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.
from random import randint as rnd


def func_rnd_num(start: int, stop: int, attempts: int):
    rnd_num = rnd(start, stop+1)
    while attempts != 0:
        user_num = int(
            input(f'Введите число от {start} до {stop}: '))
        if rnd_num < user_num:
            print('ваше число больше заданного')
            attempts -= 1
        elif rnd_num > user_num:
            print('ваше число меньше заданного')
            attempts -= 1
        else:
            return True
    return False
