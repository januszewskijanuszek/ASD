from clockSortDir import clockSetup


def installSetup():
    if clockSetup.TRIAL_VERSION:
        clockSetup.SHOW_ARRAYS = True
        clockSetup.AVERAGE_TIME = False
    if clockSetup.CLOCK_LENGTH <= 0:
        raise Exception("clockSetup.CLOCK_LENGTH = " + str(clockSetup.CLOCK_LENGTH) + "! - Must be greater than 0!")
    if not clockSetup.ADD_ZEROS:
        raise Exception("clockSetup.CLOCK_LENGTH = " + str(clockSetup.ADD_ZEROS) + "! - Must be True!")
