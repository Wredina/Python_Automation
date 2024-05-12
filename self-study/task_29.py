# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

#################################################################

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5 % от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10 % перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
import decimal

bank = 0  # кошелёк
count = 0  # счётчик операций
MULTIP = 50
LIMIT_COUNT = 3  # сколько нужно сделать операций до бонуса
WEALTH = 5_000_000  # свыше этого числа начинается богатство
PERCENT_STANDART = decimal.Decimal(0.015)  # процент за снятие
PERCENT_WEALTH = decimal.Decimal(0.10)  # процент за богатство
# процент начисления за каждую третью операцию
PERCENT_BONUS = decimal.Decimal(0.03)
MIN_LIMIT_SUM_PERCENT = decimal.Decimal(30)  # минимальный налог на снятие
MAX_LIMIT_SUM_PERCENT = decimal.Decimal(600)  # максимальный налог на снятие
hystory = []


def hystory_operation(text_hystory):
    hystory.append(text_hystory)


def user_input():
    user_cash_input = input(
        'введите сумму кратную 50-ти или введите 0 для выхода: ')
    return user_cash_input


def check_limit_percent_withd(bank_money, user_cash_input):
    if user_cash_input - (user_cash_input * PERCENT_STANDART) < MIN_LIMIT_SUM_PERCENT:
        bank_money = bank_money - (user_cash_input + MIN_LIMIT_SUM_PERCENT)
    elif user_cash_input - (user_cash_input * PERCENT_STANDART) > MAX_LIMIT_SUM_PERCENT:
        bank_money = bank_money - (user_cash_input + MAX_LIMIT_SUM_PERCENT)
    else:
        bank_money = (bank_money - user_cash_input) - \
            (user_cash_input * PERCENT_STANDART)
    return bank_money
    # налог на богатство


def wealth_bank(bank_money):
    if bank_money > WEALTH:
        bank_money = bank_money - (bank_money * PERCENT_WEALTH)
        hystory_operation(
            f'Налог на богатство 10%, итого сумма: {text_sum(bank_money)}.')
        print(f'Налог на богатство 10%')
    return bank_money


# счётчик бонуса
def count_bonus(bank_money):
    global count
    count += 1
    if count % LIMIT_COUNT == 0:
        bank_money = bank_money + (bank_money * PERCENT_BONUS)
        hystory_operation(
            f'Начисление бонуса 3%, итого сумма: {text_sum(bank_money)}.')
        print(f'Начисление бонуса 3%')
    return bank_money

# функция проверки на ввод числа кратного 50-ти


def check_digit(user_input: str) -> bool | None:
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input < 0:
            return False
        elif user_input == 0:
            return None
        elif user_input % MULTIP != 0:
            return False
        else:
            return True
    else:
        return False

# функция пополнения


def refill(bank_money):
    while True:
        user_cash_input = user_input()
        if check_digit(user_cash_input):
            bank_money = wealth_bank(bank_money)
            bank_money += decimal.Decimal(user_cash_input)
            bank_money = count_bonus(bank_money)
            hystory_operation(
                f'Операция пополнения на: {user_cash_input}, итого сумма: {text_sum(bank_money)}.')
            print(f'Сумма: {text_sum(bank_money)}')
            continue
        elif check_digit(user_cash_input) is None:
            return bank_money
        else:
            bank_money = wealth_bank(bank_money)
            print('Нужно ввести положительную сумму кратную 50-ти')
            continue

# снятие


def withdrawal(bank_money):
    while True:
        user_cash_input = user_input()
        if check_digit(user_cash_input):
            bank_money = wealth_bank(bank_money)
            if decimal.Decimal(user_cash_input) > bank_money:
                print('Не достаточно средств')
                continue
            else:
                bank_money = check_limit_percent_withd(
                    bank_money, decimal.Decimal(user_cash_input))
                bank_money = count_bonus(bank_money)
                hystory_operation(
                    f'Оперяция снятия наличных на сумму: {user_cash_input} руб, итого сумма с учётом 1.5% налога: {text_sum(bank_money)}')
                print(f'Сумма с учётом 1.5% налога: {text_sum(bank_money)}')
                continue
        elif check_digit(user_cash_input) is None:
            return bank_money
        else:
            bank_money = wealth_bank(bank_money)
            print('Нужно ввести положительную сумму кратную 50-ти')
            continue


def text_sum(bank_money) -> str | int:
    if '.' in str(bank_money):
        spl_1, spl_2 = str(bank_money).split(
            '.')[0], str(bank_money).split('.')[1]
        return str(f'{spl_1}.{spl_2[:2]}')
    else:
        return bank_money


# функция с операциями

while True:
    command = input(
        'Введите команду: Пополнить, Снять, История или Выйти: ').lower()
    if command == 'выйти':
        print(f'Ваша сумма = {text_sum(bank)}')
        break
    elif command == 'пополнить':
        bank = refill(decimal.Decimal(bank))
        print(f'Сумма: {text_sum(bank)}')
        continue
    elif command == 'снять':
        bank = withdrawal(decimal.Decimal(bank))
        print(f'Сумма: {text_sum(bank)}')
        continue
    elif command == 'история':
        print(*hystory)
    else:
        print('Вы не верно ввели команду, попробуйте снова')
        continue
