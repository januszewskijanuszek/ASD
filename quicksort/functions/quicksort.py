from functions import partition


def quicksort(array, start, stop):
    if start < stop:
        partitionResult = partition.partition(array, start, stop)
        quicksort(array, start, partitionResult - 1)
        quicksort(array, partitionResult + 1, stop)
