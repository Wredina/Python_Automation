# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s(кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце

def func():
    dt = {}
    for i in globals():
        if not i.startswith('__'):
            if i.endswith('s') and len(i) > 1:
                dt[i[:-1]] = globals()[i]
                dt[i] = None
            else:
                dt[i] = globals()[i]
    return dt


start = 1000
s = 'str'
apples = 25
codes = 546

print(func())
