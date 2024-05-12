# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def func(**kwargs) -> dict:
    new_dic = {}
    for value, key in kwargs.items():
        new_dic[key] = value

    return new_dic


print(func(a=12, b='st', c=2))
