def up(position):
    x, y = position
    return (x, y - 1)

def down(position):
    x, y = position
    return (x, y + 1)

def right(position):
    x, y = position
    return (x + 1, y)

def left(position):
    x, y = position
    return (x - 1, y)

def isWithinBounds(position):
    x, y = position
    return 0 <= x < width and 0 <= y < height

def getCell(rows, position):
    x, y = position
    return rows[y][x]

def setCell(rows, position, newValue):
    x, y = position
    rows[y][x] = newValue

def goIfPossible(rows, positions, position, previousPosition, movement, significantBit):
    cell = int(getCell(rows, position), 16)
    if cell & significantBit == 0:
        newPosition = movement(position)
        if newPosition != previousPosition:
            positions.append((newPosition, position))

def goUpIfPossible(rows, positions, position, previousPosition):
    goIfPossible(rows, positions, position, previousPosition, up, 8)

def goDownIfPossible(rows, positions, position, previousPosition):
    goIfPossible(rows, positions, position, previousPosition, down, 2)

def goRightIfPossible(rows, positions, position, previousPosition):
    goIfPossible(rows, positions, position, previousPosition, right, 4)

def goLeftIfPossible(rows, positions, position, previousPosition):
    goIfPossible(rows, positions, position, previousPosition, left, 1)

def getStartPosition():
    # Test start position to the TOP of the maze
    y = 0
    for x in range(width):
        position = (x, y)
        cell = int(getCell(rows, position), 16)
        if cell & 8 == 0:
            return position

    # Test start position to the BOTTOM of the maze
    y = height - 1
    for x in range(width):
        position = (x, y)
        cell = int(getCell(rows, position), 16)
        if cell & 2 == 0:
            return position

    # Test start position to the LEFT side of the maze
    x = 0
    for y in range(height):
        position = (x, y)
        cell = int(getCell(rows, position), 16)
        if cell & 1 == 0:
            return position

    # Test start position to the RIGHT side of the maze
    x = width - 1
    for y in range(height):
        position = (x, y)
        cell = int(getCell(rows, position), 16)
        if cell & 4 == 0:
            return position

    return None


while True:
    height, width = list(map(int, input().split()))
    if height == 0 and width == 0:
        break

    rows = []
    for _ in range(height):
        row = list(input())
        rows.append(row)

    startPosition = (getStartPosition(), None)
    positions = [startPosition]
    numberOfExits = 0
    numberOfReachedCells = 0
    hasMultiplePaths = False
    while positions:
        position, previousPosition = positions.pop()
        if not isWithinBounds(position):
            numberOfExits += 1
            continue

        cell = getCell(rows, position)
        if cell == "X":
            hasMultiplePaths = True
            continue

        numberOfReachedCells += 1

        goUpIfPossible(rows, positions, position, previousPosition)
        goDownIfPossible(rows, positions, position, previousPosition)
        goRightIfPossible(rows, positions, position, previousPosition)
        goLeftIfPossible(rows, positions, position, previousPosition)

        setCell(rows, position, "X")

    if numberOfExits != 2:
        print("NO SOLUTION")
    elif numberOfReachedCells != width * height:
        print("UNREACHABLE CELL")
    elif hasMultiplePaths:
        print("MULTIPLE PATHS")
    else:
        print("MAZE OK")
