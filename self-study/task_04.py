# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.


num = int(input("введите число "))
step = 1
spase = num

for _ in range(num):
    print(" " * (spase - 1), "*" * step)
    step += 2
    spase -= 1
