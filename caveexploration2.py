def isWithinBounds(rows, x, y):
    isXWithinBounds = 0 <= x < caveSize
    isYWithinBounds = 0 <= y < caveSize
    return isXWithinBounds and isYWithinBounds

def getEntry(rows, x, y):
    if isWithinBounds(rows, x, y):
        return rows[x][y]
    else:
        return None

def setEntry(rows, x, y, value):
    if isWithinBounds(rows, x, y):
        rows[x][y] = value

def traverse(rows, computedRows):
    stack = []
    stack.append((0, 0, 0))
    while 0 < len(stack):
        x, y, prevValue = stack.pop()

        if not isWithinBounds(rows, x, y):
            continue

        entry = getEntry(rows, x, y)
        value = max(prevValue, entry)
        bestEntry = getEntry(computedRows, x, y)
        if value < bestEntry:
            setEntry(computedRows, x, y, value)
            stack.append((x - 1, y, value))
            stack.append((x + 1, y, value))
            stack.append((x, y - 1, value))
            stack.append((x, y + 1, value))


maxValue = 10 ** 8
caveSize = int(input())
rows = []
computedRows = []
for _ in range(caveSize):
    row = list(map(int, input().split()))
    rows.append(row)
    computedRow = list(map(lambda value: maxValue, row.copy()))
    computedRows.append(computedRow)

traverse(rows, computedRows)
numberOfHoursToExit = getEntry(computedRows, caveSize - 1, caveSize - 1)
print(numberOfHoursToExit)
