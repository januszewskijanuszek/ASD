import sys

from functions import quicksort
from time import time
from random import randrange


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    array = []
    LENGTH = 1000
    for x in range(LENGTH):
        # array.append(randrange(1, 255))
        # array.append(x % 255)
        array.append(LENGTH - x)
    start = time()
    quicksort.quicksort(array, 0, len(array) - 1)
    print(LENGTH)
    print(time() - start)
    # print(array)

