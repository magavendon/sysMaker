#----------------------------------------------------------------------------------------
#   Project:    sysMaker
#   File:       stars.py
#   Desc:       This file is used to handle any functions or objects related to stars.
#----------------------------------------------------------------------------------------
version = '2'

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
    log('In Get Stars\nRandom = {}'.format(random))
    # Determine the number of stars
    numberOfStars = amountOfStars(random)
    if numberOfStars == 0:
        log('User chose an amount of stars')
        return []

    log('User chose to Go Back')
    return ['he']

def amountOfStars(random):
    log('In Amount Of Stars\nRandom = {}'.format(random))
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
        if selection == 4:
            log('User chose to Go Back')
            return 0
        elif selection == 5:
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
    mass = 0
    age = 0
    luminosity = 0
    temperature = 0
    radius = 0
    companion = False
    orbit = 0
    eccentricity = (0, 0)
    orbitalZones = (0, 0, 0)
    forbiddenZone = (0, 0)
