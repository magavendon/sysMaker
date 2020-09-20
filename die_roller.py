from random import randint

class Die_Roller():
    def roll(self, request):
        # Determine number of dice and type
        parse    = request.split('d')
        number   = int(parse[0])
        die_type = int(parse[1])

        # Roll the dice
        total = 0
        for i in range(0, number):
            total += randint(1, die_type)
        return total

dice = Die_Roller()
