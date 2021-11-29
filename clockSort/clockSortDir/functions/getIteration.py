from clockSortDir import clockSetup


# Determines how many iterations the algorithm must perform
def clockIteration(array):
    ARRAY_LENGTH = len(array)

    iteration = int(ARRAY_LENGTH / clockSetup.CLOCK_LENGTH) + 1
    if ARRAY_LENGTH % clockSetup.CLOCK_LENGTH == 0:
        iteration = iteration - 1
    return iteration
