#----------------------------------------------------------------------------------------
#   Project:    sysMaker
#   File:       menu.py
#   Desc:       This file is used for menus.
#----------------------------------------------------------------------------------------
version = '1'

def useMenu(choices):
    numberOfChoices = len(choices)

    userChoice = 0
    while userChoice < 1 or userChoice > int(numberOfChoices):
        print()

        for choiceIndex in range(0, numberOfChoices):
            choice = choices[choiceIndex]
            print('[{}] {}'.format(choiceIndex + 1, choice))

        try:
            userChoice = int(input('> '))
            if userChoice < 1 or userChoice > int(numberOfChoices):
                raise ValueError('Choice not an option')
        except ValueError:
            print('Please choose one of the available options.')

    return userChoice
