numberOfRounds = int(input())
svenSymbols = input()
numberOfFriends = int(input())

symbolsInRounds = []
for _ in range(numberOfRounds):
    friendsSymbols = {
        "R": 0,
        "P": 0,
        "S": 0,
    }
    symbolsInRounds.append(friendsSymbols)

for _ in range(numberOfFriends):
    friendSymbols = input()
    for round in range(numberOfRounds):
        friendSymbol = friendSymbols[round]
        symbolsInRounds[round][friendSymbol] += 1

totalScore = 0
bestPossibleScore = 0
for round in range(numberOfRounds):
    svenSymbol = svenSymbols[round]
    symbolFromFriends = symbolsInRounds[round]
    scoreForRock = 2 * symbolFromFriends["S"] + 1 * symbolFromFriends["R"] + 0 * symbolFromFriends["P"]
    scoreForPaper = 2 * symbolFromFriends["R"] + 1 * symbolFromFriends["P"] + 0 * symbolFromFriends["S"]
    scoreForScissor = 2 * symbolFromFriends["P"] + 1 * symbolFromFriends["S"] + 0 * symbolFromFriends["R"]
    bestPossibleScore += max(scoreForRock, scoreForPaper, scoreForScissor)
    if svenSymbol == "R":
        totalScore += scoreForRock
    elif svenSymbol == "P":
        totalScore += scoreForPaper
    elif svenSymbol == "S":
        totalScore += scoreForScissor

print(totalScore)
print(bestPossibleScore)
