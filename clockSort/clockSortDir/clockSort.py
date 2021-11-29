from clockSortDir.functions import clockSplitter
from clockSortDir import clockSetup


def clockSort(array):
    mainArray = clockSplitter.arraySplitter(array)
    mainArrayLength = len(mainArray)
    if clockSetup.SHOW_ARRAYS:
        print("Array INPUT")
        print(mainArray, "Length -> ", mainArrayLength)

    # ONLY Last feature
    stabilizer = 0
    if clockSetup.ONLY_LAST_CLOCK:
        stabilizer = mainArrayLength - 1
    for mainClock in range(mainArrayLength - stabilizer):
        if clockSetup.ONLY_LAST_CLOCK:
            mainClock = mainArrayLength - 1
        for mainClockNumbers in range(clockSetup.CLOCK_LENGTH):
            for clocks in range(mainArrayLength):
                for clocksNumbers in range(clockSetup.CLOCK_LENGTH):
                    if clockSetup.REVERSE:
                        if mainArray[mainClock][mainClockNumbers] > mainArray[clocks][clocksNumbers]:
                            mainArray[mainClock][mainClockNumbers], mainArray[clocks][clocksNumbers] = \
                                mainArray[clocks][clocksNumbers], mainArray[mainClock][mainClockNumbers]
                    else:
                        if mainArray[mainClock][mainClockNumbers] < mainArray[clocks][clocksNumbers]:
                            mainArray[mainClock][mainClockNumbers], mainArray[clocks][clocksNumbers] = \
                                mainArray[clocks][clocksNumbers], mainArray[mainClock][mainClockNumbers]
    if clockSetup.SHOW_ARRAYS:
        print("Array OUTPUT")
        print(mainArray)
    return mainArray
