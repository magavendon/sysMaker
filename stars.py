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
    if not random:
        log('Doing choice')
        choices = ['1 star',
                   '2 stars',
                   '3 stars',
                   'Random',
                   'Go back',
                   'Quit']
        selection = useMenu(choices)
        if selection <= 3:
          log('User chose an amount of stars\nLeaving Amount of Stars')
          return selection
        if selection == 4:
            random = True
        if selection == 5:
            log('User chose to Go Back')
            return 0
        elif selection == 6:
            log('User chose to Quit')
            quit()


    if random:
        pass

#----------------------------------------------------------------------------------------
#  ██████  ██████       ██ ███████  ██████ ████████ ███████
# ██    ██ ██   ██      ██ ██      ██         ██    ██
# ██    ██ ██████       ██ █████   ██         ██    ███████
# ██    ██ ██   ██ ██   ██ ██      ██         ██         ██
#  ██████  ██████   █████  ███████  ██████    ██    ███████
#----------------------------------------------------------------------------------------
class Star:
    RANDOM = False

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

    def __init__(self, random):
        self.RANDOM = random

    def getMass(self):
        random = self.RANDOM
        if not random:
            choices = []
            selection = useMenu(choices)
            if selection == 1:
                pass
            elif selection == 2:
                pass

        if random:
            pass
