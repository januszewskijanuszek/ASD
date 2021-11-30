# Welcome in clock sort v1.0 by Patryk Januszewski s22638
# --------------------------------------------------------
# You can change default settings in functions/clockSetup!

from clockSortDir import clockSort
from clockSortDir import clockSetup
from clockSortDir.functions.installSetup import installSetup
import time
import random

NUM_OF_NUMS = 80000


def main():
    if clockSetup.TRIAL_VERSION:
        array = [1, 3, 5, 7, 12, 45, 32, 13, 4]
        start = time.time()
        clockSort.clockSort(array)
        return time.time() - start
    elif clockSetup.AVERAGE_TIME:
        return averageTime()
    else:
        array = []
        for x in range(NUM_OF_NUMS):
            # array.append(random.randrange(1, 255))
            # array.append(x)
            array.append(NUM_OF_NUMS - x)
        start = time.time()
        clockSort.clockSort(array)
        return time.time() - start


def averageTime():
    COUNTIES = 10
    timeSum = 0
    for i in range(COUNTIES):
        array = []
        for x in range(NUM_OF_NUMS):
            array.append(random.randrange(1, 100))
        start = time.time()
        clockSort.clockSort(array)
        timeSum += time.time() - start
        print(((i + 1) / COUNTIES) * 100, "%")
    return timeSum / COUNTIES


if __name__ == "__main__":
    installSetup()
    message = ""
    if clockSetup.AVERAGE_TIME:
        message = " <- Average Time"
    print("--- %s seconds---" % main(), message)
