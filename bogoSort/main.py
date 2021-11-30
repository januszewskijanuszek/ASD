import random
import time

if __name__ == '__main__':
    REVERSE = False
    array = []
    for x in range(11):
        array.append(random.randrange(1, 255))
    done = False
    start = time.time()
    while not done:
        random.shuffle(array)
        for x in range(len(array) - 1):
            if REVERSE:
                if array[x] >= array[x + 1]:
                    done = True
                else:
                    done = False
                    break
            else:
                if array[x] <= array[x + 1]:
                    done = True
                else:
                    done = False
                    break
    print("Time: ", time.time() - start)
    print(array)