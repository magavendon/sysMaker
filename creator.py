#----------------------------------------------------------------------------------------
#   Project:    sysMaker
#   File:       creator.py
#   Desc:       This is the main file for running the entire program.
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
from stars import getStars

#----------------------------------------------------------------------------------------
# ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████
#----------------------------------------------------------------------------------------
# Main Menu
def mainMenu():
    log('Begin Main Menu')

    # Main menu options
    choices = ['Random System',
               'Optional System',
               'Quit']
    selection = useMenu(choices)

    # Perform correct action
    if selection == 1:
        log('User chose Random')
        # Create a completely random system
        createSystem()
    elif selection == 2:
        log('User chose Optional')
        # Give the user options for creating a system
        createSystem(False)
    elif selection == 3:
        log('User chose Quit')
        # Quit the program
        quit()

# Create system
def createSystem(random = True):
    log('In Create System\nRandom = {}'.format(str(random)))
    # Get the system's stars
    stars = []
    stars = getStars()
    if len(stars) == 0:
        mainMenu()

#----------------------------------------------------------------------------------------
# ██████  ███████  ██████  ██ ███    ██
# ██   ██ ██      ██       ██ ████   ██
# ██████  █████   ██   ███ ██ ██ ██  ██
# ██   ██ ██      ██    ██ ██ ██  ██ ██
# ██████  ███████  ██████  ██ ██   ████
#----------------------------------------------------------------------------------------
log('Start Creator', True)

title = '*******************************************************************\n'
title += '███████ ██    ██ ███████ ███    ███  █████  ██   ██ ███████ ██████\n'
title += '██       ██  ██  ██      ████  ████ ██   ██ ██  ██  ██      ██   ██\n'
title += '███████   ████   ███████ ██ ████ ██ ███████ █████   █████   ██████\n'
title += '     ██    ██         ██ ██  ██  ██ ██   ██ ██  ██  ██      ██   ██\n'
title += '███████    ██    ███████ ██      ██ ██   ██ ██   ██ ███████ ██   ██\n'
title += '*******************************************************************'

# Print title
print(title)

# Go to main menu
mainMenu()

log('End Creator')
