# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.


def answer_riddle(riddle: str, answers: list, attempts: int) -> int:
    cnt = 1
    answers = list(map(lambda x: x.lower(), answers))
    print(answers)
    while attempts:
        print(riddle)
        user_answer = input('Ваш ответ: ').lower()
        if user_answer in answers:
            return cnt
        else:
            cnt += 1
            attempts -= 1
            print(f'неверный ответ, осталось попыток {attempts}')
    return 0
