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
from random import randit
# Project File Imports
from logger import log
from menu import useMenu
from roll import *

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

  # Set the Stellar Mass
  def setStellarMass(self, roll1, roll2 = None):
    bigSmudge = [
        -.04,-.03,-.03,-.02,-.02,-.02,-.01,-.01,-.01,-.01,0,0,0,0,0,0,.01,.01,
        .01,.01,.01,.02,.02,.02,.02,.03,.03,.03,.04,.04,.05]
    bigSmudge = bigSmudge[randint(0,len(bigSmudge)-1)]
    smallSmudge = [-.02,-.01,-.01,0,0,0,0,.01,.01,.01,.02,.02,.03]
    smallSmudge = smallSmudge[randint(0,len(smallSmudge)-1)]

    # Set the Stellar Mass based on the table.
    if roll2:
      if   roll1 ==  2:
        if roll2 < 11:
          self.mass = 2.20 + bigSmudge
        else:
          self.mass = 2.10 + bigSmudge
      elif roll1 ==  3:
        if roll2 < 11:
          self.mass = 2.00 + bigSmudge
        else:
          self.mass = 1.90 + bigSmudge
      elif roll1 ==  4:
        if   roll2 <  9:
          self.mass = 1.80 + bigSmudge
        elif roll2 < 12:
          self.mass = 1.70 + bigSmudge
        else:
          self.mass = 1.60 + bigSmudge
      elif roll1 ==  5:
        if   roll2 <  8:
          self.mass = 1.50 + randint(-2, 5)
        elif roll2 < 11:
          self.mass = 1.45 + smallSmudge
        elif roll2 < 13:
          self.mass = 1.40 + smallSmudge
        else:
          self.mass = 1.35 + smallSmudge
      elif roll1 ==  6:
        if   roll2 <  8:
          self.mass = 1.30 + smallSmudge
        elif roll2 < 10:
          self.mass = 1.25 + smallSmudge
        elif roll2 < 11:
          self.mass = 1.20 + smallSmudge
        elif roll2 < 13:
          self.mass = 1.15 + smallSmudge
        else:
          self.mass = 1.10 + smallSmudge
      elif roll1 ==  7:
        if   roll2 <  8:
          self.mass = 1.05 + smallSmudge
        elif roll2 < 10:
          self.mass = 1.00 + smallSmudge
        elif roll2 < 11:
          self.mass = 0.95 + smallSmudge
        elif roll2 < 13:
          self.mass = 0.90 + smallSmudge
        else:
          self.mass = 0.85 + smallSmudge
      elif roll1 ==  8:
        if   roll2 <  8:
          self.mass = 0.80 + smallSmudge
        elif roll2 < 10:
          self.mass = 0.75 + smallSmudge
        elif roll2 < 11:
          self.mass = 0.70 + smallSmudge
        elif roll2 < 13:
          self.mass = 0.65 + smallSmudge
        else:
          self.mass = 0.60 + smallSmudge
      elif roll1 ==  9:
        if   roll2 <  9:
          self.mass = 0.55 + smallSmudge
        elif roll2 < 12:
          self.mass = 0.50 + smallSmudge
        else:
          self.mass = 0.45 + smallSmudge
      elif roll1 == 10:
        if   roll2 <  9:
          self.mass = 0.40 + smallSmudge
        elif roll2 < 12:
          self.mass = 0.35 + smallSmudge
        else:
          self.mass = 0.30 + smallSmudge
      elif roll1 == 11:
        if roll2 < 11:
          self.mass = 0.25 + smallSmudge
        else:
          self.mass = 0.20 + smallSmudge
      else:
        if roll2 < 11:
          self.mass = 0.15 + smallSmudge
        else:
          self.mass = 0.10 + smallSmudge
    else:
      # TODO Figure out how to compare to the primary star.
      pass

  def getMass(self):
    random = self.RANDOM
    if not random:
      choices = ['Select mass',
                 'Random mass']
      selection = useMenu(choices)
    if selection == 1:
      pass
    elif selection == 2:
      random = True

    if random:
      if not companion:
        # Generate size like normal (with my special changes).

        # Use 2 dice instead of 3 because the average is closer to Sol.
        firstRoll = rollDice(2, 6)
        secondRoll = rollDice(3, 6)

        # Set the stellar mass based on the table.
        setStellarMass(firstRoll, secondRoll)
      else:
        # Generate size based on primary.

        # Figure out if the companion has the same mass as the primary.
        diceToRoll = rollDie(6) - 1
        if diceToRoll == 0:
          # TODO Figure out how to compare to the primary star.
          # Use pretty much the same solar mass as the primary.
          pass
        else:
          # Figure out how many entries to go down the table.
          roll = rollDice(diceToRoll, 6)

          # Set the stellar mass based on the table.
          setStellarMass(roll)

