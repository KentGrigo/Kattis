numberOfPieces = int(input())
pieces = list(map(int, input().split()))
pieces.sort(reverse = True)

isAlicesTurn = True
sumAlice = 0
sumBob = 0
for piece in pieces:
    if isAlicesTurn:
        sumAlice += piece
    else:
        sumBob += piece

    isAlicesTurn = not isAlicesTurn

print(sumAlice, sumBob)
