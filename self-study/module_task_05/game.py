# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку(текст загадки) и число(номер попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение.


def answer_riddle(riddle, answers, attempts):
    cnt = 1
    while attempts + 1 != cnt:
        print(riddle)
        user_answer = input('Ваш ответ: ').lower()
        print('\n')
        if user_answer in answers:
            return cnt
        else:
            cnt += 1
    else:
        return 0


def generate_riddles(riddles, attempts):
    for riddle, answer in riddles.items():
        answ_att = answer_riddle(riddle, answer, attempts)
        record_result(riddle, answ_att)


def record_result(riddle: str, attempts: int):
    global _result
    _result[riddle] = attempts


def print_result(_result: dict):
    for riddle, att in _result.items():
        if att == 0:
            print(f'загадку {riddle} вы не смогли угадать')
        else:
            print(f'загадку {riddle} вы смогли угадать c {att} раза')


_result = {}
riddles = {'riddle_1': ['text1', 'text2'], 'riddle2': [
    'text3', 'text4', 'text5'], 'riddle3': ['text6', 'text7', 'text8', 'text9', 'text10']}
generate_riddles(riddles, 4)
print_result(_result)
