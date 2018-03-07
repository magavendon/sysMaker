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
  if showIndividualRolls:
    rolls = []
  sumOfRolls = 0
  # Roll each die.
  for rollNumber in range(0, amount):
    rollResult = rollDie(dieType)
    sumOfRolls += rollResult
    if showIndividualRolls:
      rolls.append(rollResult)

  # Return results.
  if showIndividualRolls:
    individualRolls = ', '.join(str(roll) for roll in rolls)
    return 'Rolls: {}\n  Sum: {}'.format(individualRolls, sumOfRolls)
  return sumOfRolls

#----------------------------------------------------------------------------------------
# ██    ██ ███    ██ ██ ████████     ████████ ███████ ███████ ████████
# ██    ██ ████   ██ ██    ██           ██    ██      ██         ██
# ██    ██ ██ ██  ██ ██    ██           ██    █████   ███████    ██
# ██    ██ ██  ██ ██ ██    ██           ██    ██           ██    ██
#  ██████  ██   ████ ██    ██           ██    ███████ ███████    ██
#----------------------------------------------------------------------------------------
if __name__ == '__main__':
  roll = None
  for x in range(0,1000):
    roll = rollDie(6)
  print(roll)

  customFaces = ['hello', 'world', 'foo', 'bar', 'boo', 'baz']
  for x in range(0, 1000):
    roll = rollCustomDie(customFaces)
  print(roll)

  roll = [None, None, None, None]
  for x in range(0, 4):
    for y in range(0, 250):
      roll[0] = rollDice(2, 4)
    for y in range(0, 250):
      roll[1] = rollDice(3, 4)
    for y in range(0, 250):
      roll[2] = rollDice(4, 4)
    for y in range(0, 250):
      roll[3] = rollDice(5, 4)
  print(roll)

  for x in range(0, 4):
    for y in range(0, 250):
      roll[0] = rollDice(2, 4, True)
    for y in range(0, 250):
      roll[1] = rollDice(3, 4, True)
    for y in range(0, 250):
      roll[2] = rollDice(4, 4, True)
    for y in range(0, 250):
      roll[3] = rollDice(5, 4, True)
  print(roll)
