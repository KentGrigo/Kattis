class Player:
    def __init__(self, dice1, dice2):
        self.maxDice = max(dice1, dice2)
        self.minDice = min(dice1, dice2)

    def __str__(self):
        return "({}, {})".format(self.maxDice, self.minDice)

    def isMia(self):
        return self.maxDice == 2 and self.minDice == 1

    def isPair(self):
        return self.maxDice == self.minDice

    def __eq__(self, other):
        return self.maxDice == other.maxDice and self.minDice == other.minDice

    def compare(self, other):
        if self.__eq__(other):
            return 0
        elif self.isMia():
            return 1
        elif other.isMia():
            return -1
        elif self.isPair() and not other.isPair():
            return 1
        elif not self.isPair() and other.isPair():
            return -1
        elif self.maxDice < other.maxDice or \
            (self.maxDice == other.maxDice and self.minDice < other.minDice):
            return -1
        else:
            return 1

while True:
    data = input().split()
    player1Dice1 = int(data[0])
    player1Dice2 = int(data[1])
    player2Dice1 = int(data[2])
    player2Dice2 = int(data[3])
    if player1Dice1 == 0 and player1Dice2 == 0 and player2Dice1 == 0 and player2Dice2 == 0:
        break

    player1 = Player(player1Dice1, player1Dice2)
    player2 = Player(player2Dice1, player2Dice2)

    isPlayer1Winner = player1.compare(player2)
    if isPlayer1Winner == 1:
        print("Player 1 wins.")
    elif isPlayer1Winner == -1:
        print("Player 2 wins.")
    else:
        print("Tie.")
