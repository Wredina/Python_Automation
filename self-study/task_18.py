# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friends = {'vasya': ('спальник', 'чайник', 'кастрюля'),
           'ilya': ('спальник', 'вилка', 'нож'),
           'katya': ('зажигалка', 'ложка', 'палатка')}

# items_uni = set.union(*[set(i) for i in friends.values()])

items_uni = set()

for i in friends.values():
    items_uni.update(set(i))

print(f'Какие вещи взяли все три друга {items_uni}', end='\n\n')

items_sym_dif = items_uni.copy()
items_dif = items_uni.copy()
for i in friends.values():
    items_sym_dif.symmetric_difference_update(set(i))

items_dif -= items_sym_dif

print(f'Какие вещи уникальны, есть только у одного друга {items_dif}')

missing_items = {}

for friend, i in friends.items():
    # print(str(items_sym_dif) in set(i))
    if items_sym_dif.isdisjoint(set(i)):
        print(f"Какие вещи есть у всех друзей кроме одного:{
              items_sym_dif}, у кого данная вещь отсутствует {friend}")
    else:
        continue
