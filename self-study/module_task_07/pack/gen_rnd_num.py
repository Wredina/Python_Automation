# Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.
from random import randint as rnd


def func_rnd_num(start: int, stop: int, attempts: int):
    rnd_num = rnd(start, stop)
    while attempts != 0:
        user_num = int(
            input(f'Введите число в пределах от {start} до {stop}: '))
        if rnd_num < user_num:
            print('ваше число больше заданного')
            attempts -= 1
        elif rnd_num > user_num:
            print('ваше число меньше заданного')
            attempts -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    print(func_rnd_num(1, 10, 5))
