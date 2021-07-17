numberOfPairs = int(input())
originalPile = list(map(int, input().split()))

numberOfMoves = 0
auxiliaryPile = []
while originalPile:
    numberOfMoves += 1
    if auxiliaryPile and originalPile[-1] == auxiliaryPile[-1]:
        originalPile.pop()
        auxiliaryPile.pop()
    else:
        sock = originalPile.pop()
        auxiliaryPile.append(sock)

if originalPile or auxiliaryPile:
    print("impossible")
else:
    print(numberOfMoves)
