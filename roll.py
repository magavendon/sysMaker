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
import random

#----------------------------------------------------------------------------------------
# ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████
#----------------------------------------------------------------------------------------
def rollDie(dieType):
  return random.randint(1,dieType)

def rollCustomDie(customFaces):
  # Figure out how many sides the die has.
  dieType = len(customFaces)
  # Get the roll.
  roll = rollDie(dieType)
  # Return the face that was rolled (subtract 1 to account for the list
  # starting at zero).
  return customFaces[roll - 1]

def rollDice(amount, dieType, showIndividualRolls = False):
  # Define rolls list of showing individual rolls.
  rolls = [] if showIndividualRolls else pass
  sumOfRolls = 0
  # Roll each die.
  for rollNumber in range(0, amount):
    rollResult = rollDie(dieType)
    sumOfRolls += rollResult
    rolls.append(rollResult) if showIndividualRolls else pass

  # Return results.
  if showIndividualRolls:
    individualRolls = ', '.join(str(roll) for roll in rolls)
    return 'Rolls: {}\n  Sum: {}'.format(individualRolls, sumOfRolls)
  return sumOfRolls
