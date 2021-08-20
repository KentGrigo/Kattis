# Move no. 1: head - 1 -> head + 1
# Move no. 2: tail - 1 -> tail + 2
# Move no. 3: head - 2 ->
# Move no. 4: tail - 2 -> head + 1
class Hydra:
    def __init__(self, numberOfHeads, numberOfTails):
        self.numberOfHeads = numberOfHeads
        self.numberOfTails = numberOfTails

    def isDead(self):
        return self.numberOfHeads == 0 and self.numberOfTails == 0

    def move1(self):
        self.numberOfHeads -= 1
        self.numberOfHeads += 1

    def move2(self):
        self.numberOfTails -= 1
        self.numberOfTails += 2

    def move3(self):
        self.numberOfHeads -= 2

    def move4(self):
        self.numberOfTails -= 2
        self.numberOfHeads += 1

while True:
    numberOfHeads, numberOfTails = list(map(int, input().split()))
    if numberOfHeads == 0 and numberOfTails == 0:
        break

    numberOfMoves = 0
    hydra = Hydra(numberOfHeads, numberOfTails)
    while not hydra.isDead():
        numberOfMoves += 1
        if 2 <= hydra.numberOfHeads:
            hydra.move3()
        elif 4 <= hydra.numberOfTails:
            hydra.move4()
        elif hydra.numberOfTails % 2 == 1:
            hydra.move2()
        elif hydra.numberOfHeads % 2 == 0 and \
                hydra.numberOfTails % 2 == 0 and \
                0 < hydra.numberOfTails:
            hydra.move2()
        elif hydra.numberOfHeads % 2 == 1 and \
                0 < hydra.numberOfTails:
            hydra.move4()
        else:
            break

    if hydra.isDead():
        print(numberOfMoves)
    else:
        print(-1)
