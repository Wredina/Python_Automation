# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25 %». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = ['12.1 %', '10.25 %', '15.13 %', '9.99 %']
us_dict = ({names[i]: salaries[i] *
           float(awards[i][:-1]) / 100} for i in range(len(names)))

for i in us_dict:
    print(i)
