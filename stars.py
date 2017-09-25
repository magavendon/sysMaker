#----------------------------------------------------------------------------------------
#   Project:    sysMaker
#   File:       stars.py
#   Desc:       This file is used to handle any functions or objects related to stars.
#----------------------------------------------------------------------------------------
version = '1'

#----------------------------------------------------------------------------------------
# ██ ███    ███ ██████   ██████  ██████  ████████ ███████
# ██ ████  ████ ██   ██ ██    ██ ██   ██    ██    ██
# ██ ██ ████ ██ ██████  ██    ██ ██████     ██    ███████
# ██ ██  ██  ██ ██      ██    ██ ██   ██    ██         ██
# ██ ██      ██ ██       ██████  ██   ██    ██    ███████
#----------------------------------------------------------------------------------------
# Default Python Imports
from sys import exit as quit
# Project File Imports
from logger import log
from menu import useMenu

#----------------------------------------------------------------------------------------
# ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████
#----------------------------------------------------------------------------------------
def getStars(random = True):
    log('In Get Stars')
    # Determine the number of stars
    numberOfStars = amountOfStars(random)
    if numberOfStars == 0:
        log('User chose an amount of stars')
        return []

    log('User chose to Go Back')
    return ['he']

def amountOfStars(random):
    log('In Amount Of Stars')
    if random:
        log('Passing on random')
        pass
    else:
        log('Doing choice')
        choices = ['1 star',
                   '2 stars',
                   '3 stars',
                   'Go back',
                   'Quit']
        selection = useMenu(choices)
        if selection == 3:
            log('User chose to Go Back')
            return 0
        elif selection == 4:
            log('User chose to Quit')
            quit()

        log('User chose an amount of stars\nLeaving Amount of Stars')
        return selection

#----------------------------------------------------------------------------------------
#  ██████  ██████       ██ ███████  ██████ ████████ ███████
# ██    ██ ██   ██      ██ ██      ██         ██    ██
# ██    ██ ██████       ██ █████   ██         ██    ███████
# ██    ██ ██   ██ ██   ██ ██      ██         ██         ██
#  ██████  ██████   █████  ███████  ██████    ██    ███████
#----------------------------------------------------------------------------------------
class Star:
    pass
