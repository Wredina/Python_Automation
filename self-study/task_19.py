# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def text(txt: str) -> str:
    txt = sorted(txt.split())
    big_word = len(max(txt, key=len)) + 1
    for num, word in enumerate(txt, start=1):
        print(f'{num} {word:>{big_word}}')


text('Вывести функцией каждое слово с новой строки')
