#----------------------------------------------------------------------------------------
#   Project:    sysMaker
#   File:       menu.py
#   Desc:       This file is used for menus.
#----------------------------------------------------------------------------------------
version = '2'

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

def limitedNumberChoice(limits, rounding = 0):
  userChoice = None
  while not userChoice:
    print()

    # Figure out what values the user is allowed to choose between.
    betweenString = ''
    for limitIndex in range(0, len(limits)):
      limit = limits[limitIndex]
      betweenString = '{}{} and {}'.format(betweenString, limit[0], limit[1])
      if limitIndex == len(limits) - 1:
        betweenString += ': '
      else:
        betweenString += ' or '

    # Generate the prompt.
    promptString = 'Please choose a value '
    if rounding > 0:
      promptString += 'up to {} decimal places '.format(rounding)
    promptString += 'between {}'.format(betweenString)

    # Get the user's input.
    try:
      userChoice = float(input(promptString))
      brokeLimits = True
      for limit in limits:
        if userChoice >= limit[0] and userChoice <= limit[1]:
          brokeLimits = False
      if brokeLimits:
        raise ValueError('Outside of limits')
    except ValueError:
      print('Please choose a value within the limits.')
      userChoice = None

  if rounding == 0:
    return int(userChoice)
  else:
    return round(userChoice, rounding)
