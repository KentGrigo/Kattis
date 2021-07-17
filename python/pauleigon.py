servesPerTurn, paulPoints, opponentPoints = list(map(int, input().split()))
points = paulPoints + opponentPoints
numberOfTurns = points // servesPerTurn
isPaulsTurn = numberOfTurns & 1 == 0
if isPaulsTurn:
    print("paul")
else:
    print("opponent")
