def partition(array, start, stop):
    last = array[stop]
    counter = start - 1
    for i in range(start, stop):
        if array[i] <= last:
            counter = counter + 1
            array[counter], array[i] = array[i], array[counter]
    array[counter + 1], array[stop] = array[stop], array[counter + 1]
    # print(array)
    return counter + 1
