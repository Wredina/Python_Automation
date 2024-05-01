# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import math
import decimal

d = decimal.Decimal(input('d: '))

decimal.getcontext().prec = 42
s = decimal.Decimal(math.pi) * (d / 2) ** 2
c = decimal.Decimal(math.pi) * d

print(s, c, sep="\n")
