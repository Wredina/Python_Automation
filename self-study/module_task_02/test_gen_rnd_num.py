from guessing_game import func_rnd_num as f_rnd
from sys import argv

if __name__ == '__main__':
    options = list(map(int, argv[1:]))
    low_limit = 1
    hight_limit = 100
    count = 10
    if len(options) == 1:
        hight_limit = options[0]
    elif len(options) == 2:
        low_limit, hight_limit = options
    else:
        low_limit, hight_limit, count, *_ = options

    if low_limit > hight_limit:
        low_limit, hight_limit = hight_limit, low_limit

    f_rnd(low_limit, hight_limit, count)

# запуск python test_gen_rnd_num.py 10 32 546 84 231 5
