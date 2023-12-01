"""Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""


# Пример использования функции
num = int(input("num: "))
HEX = "0123456789abcdef"
hex_str = ""
print(hex(num))
while num > 0:
    hex_str = HEX[num % 16] + hex_str
    num = num // 16
print(f"Шестнадцатеричное представление числа: {hex_str}")
print('Проверка числа:', hex(num))