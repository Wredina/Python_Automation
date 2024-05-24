# Создайте функцию генератор чисел Фибоначчи
from random import randint


def fib(stop):
    fib1 = 1
    fib2 = 0
    fib3 = 0
    for _ in range(stop):
        fib3 = fib1
        fib1 += fib2
        fib2 = fib3
        yield fib1


num_stop = randint(50, 100)

print(*fib(num_stop))
