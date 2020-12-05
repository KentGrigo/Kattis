import math

data = input().split()
numberOfMatches = int(data[0])
boxWidth = int(data[1])
boxHeight = int(data[2])
boxDiagonal = math.sqrt(boxWidth ** 2 + boxHeight ** 2)

for _ in range(numberOfMatches):
    matchLength = int(input())
    doesMatchFitInBox = matchLength <= boxDiagonal
    if doesMatchFitInBox:
        print("DA")
    else:
        print("NE")
