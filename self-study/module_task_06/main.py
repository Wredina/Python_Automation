from random import randint as rnd
from data_ import real_data as rd

if __name__ == '__main__':
    gen_data = [str(rnd(1, 40)), str(rnd(1, 20)), str(rnd(1, 15_000))]
    print(gen_data)
    data = '.'.join(gen_data)
    print(rd(data))
