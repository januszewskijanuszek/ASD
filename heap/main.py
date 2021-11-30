import random
import sys
import time


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    LENGTH = 10000000
    array = []
    for x in range(LENGTH):
        # array.append(random.randrange(1, 100))
        # array.append(x)
        array.append(LENGTH - x)
    stat = time.time()
    heapSort(array)
    print(time.time() - stat)
    # print(array)
