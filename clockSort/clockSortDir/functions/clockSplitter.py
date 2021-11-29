from clockSortDir import clockSetup
from clockSortDir.functions import getIteration


# Splits original array to clocks
def arraySplitter(array):
    splitArray = []

    iteration = getIteration.clockIteration(array)
    for i in range(iteration):
        temporaryArray = []
        for j in range(clockSetup.CLOCK_LENGTH):
            try:
                # Try save number from list to tempList
                temporaryArray.append(array[j + (clockSetup.CLOCK_LENGTH * i)])
            except:
                if clockSetup.ADD_ZEROS:
                    # The algorithm will add zeros to make the clock full
                    temporaryArray.append(0)
        splitArray.append(temporaryArray)
    return splitArray
