# Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.
def answer_riddle(riddle: dict, attempts: int):
    for key, value in riddle.items():
        cnt = 1
        while attempts != cnt:
            print(key)
            user_answer = input('Ваш ответ: ').lower()
            if user_answer in value:
                yield cnt
                break
            else:
                cnt += 1
                print(f'неверный ответ')
        else:
            yield 0


def generate_riddles(attempts):
    riddles = {'riddle_1': ['text1', 'text2'], 'riddle2': [
        'text3', 'text4', 'text5'], 'riddle3': ['text6', 'text7', 'text8', 'text9', 'text10']}
    for i in answer_riddle(riddles, attempts):
        print(i)
