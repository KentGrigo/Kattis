def getIndex(rowNumber, columnNumber):
    return rowNumber * numberOfColumns + columnNumber


numberOfRows, numberOfColumns, numberOfMines = list(map(int, input().split()))
field = ['.'] * (numberOfColumns * numberOfRows)
for _ in range(numberOfMines):
    rowNumber, columnNumber = list(map(int, input().split()))
    index = getIndex(rowNumber - 1, columnNumber - 1)
    field[index] = '*'

for rowNumber in range(numberOfRows):
    fromIndex = getIndex(rowNumber, 0)
    toIndex = getIndex(rowNumber + 1, 0)
    row = field[fromIndex:toIndex]
    output = ''.join(row)
    print(output)
