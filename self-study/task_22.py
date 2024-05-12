# Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

from random import randint


def sort_list(li: list):
    for i in range(1, len(li)):
        for j in range(len(li) - i):  # все большие элементы протаскиваются вправо и их уже трогать нет смысла, поэтому после каждого завершённого цикла j отнимаем сётчик i (отнимаем с конца)
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


rand_list = [randint(1, 20) for i in range(20)]

print(rand_list)
sort_list(rand_list)
print(rand_list)
