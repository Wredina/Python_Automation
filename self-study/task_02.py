# Посчитайте сумму чётных элементов от 1 до n исключая кратные е.
# используя while if

n = int(input("введите число "))
e = int(input("крастность "))
sum = 0

while n > 0:
    if n % e != 0 and n % 2 == 0:
        sum += n
        print(n)
    n -= 1

print(sum)
