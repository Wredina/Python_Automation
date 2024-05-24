from data_ import real_data as rd
from sys import argv

if __name__ == '__main__':
    data = '.'.join(argv[1:])
    print(data)
    print(rd(data))
