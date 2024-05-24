# Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

str_input = 'Самостоятельно сохраните в переменной строку текста'

# my_dict = {i: ord(i) for i in str_input}
# print(my_dict)

# my_dict_iter = iter(my_dict.items())

my_dict = ({i: ord(i)} for i in str_input)

for _ in range(5):
    print(next(my_dict))
