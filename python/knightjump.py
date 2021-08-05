from collections import deque

def findKnight(rows):
    for rowIndex, row in enumerate(rows):
        if "K" in row:
            columnIndex = row.index("K")
            return (columnIndex, rowIndex)

    return None

def moveKnight(rows, x, y):
    patterns = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]

    queue = deque()
    queue.append((x, y, 0))
    while queue:
        x, y, numberOfMoves = queue.popleft()
        if x == 0 and y == 0:
            return numberOfMoves

        isWithinBounds = 0 <= x < boardSize and 0 <= y < boardSize
        if not isWithinBounds:
            continue

        field = rows[y][x]
        if field == "#":
            continue

        rows[y][x] = "#"
        for offsetX, offsetY in patterns:
            queue.append((x + offsetX, y + offsetY, numberOfMoves + 1))

    return None


boardSize = int(input())
rows = []
for _ in range(boardSize):
    row = list(input())
    rows.append(row)

knightX, knightY = findKnight(rows)
leastNumberOfMoves = moveKnight(rows, knightX, knightY)
if leastNumberOfMoves is None:
    print("-1")
else:
    print(leastNumberOfMoves)
