numberOfLines, _ = list(map(int, input().split()))
mine = '*'

numberOfMines = 0
mineCoordinates = []
for lineNumber in range(numberOfLines):
    line = input()
    for characterNumber, character in enumerate(line):
        if character == mine:
            numberOfMines += 1
            mineCoordinate = (lineNumber, characterNumber)
            mineCoordinates.append(mineCoordinate)

print(numberOfMines)
for lineNumber, characterNumber in mineCoordinates:
    print(lineNumber + 1, characterNumber + 1)
