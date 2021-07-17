from collections import deque

def isWithinBounds(x, y):
    return 0 <= x < width and 0 <= y < height

def getEntry(grid, x, y):
    if isWithinBounds(x, y):
        return grid[y][x]
    else:
        return None

def setEntry(grid, x, y, newValue):
    if isWithinBounds(x, y):
        grid[y][x] = newValue

def traverse(lines, grid, startingX, startingY):
    queue = deque()
    queue.append((startingX, startingY, -1, "S"))
    while queue:
        x, y, travelDistance, direction = queue.popleft()
        field = getEntry(lines, x, y)
        distance = getEntry(grid, x, y)
        if field is None:
            return travelDistance
        elif not ((field == "0" or field == direction) and (distance == -1 or travelDistance + 1 < distance)):
            continue

        newTravelDistance = travelDistance + 1
        setEntry(grid, x, y, newTravelDistance)
        queue.append((x + 1, y, newTravelDistance, "L"))
        queue.append((x - 1, y, newTravelDistance, "R"))
        queue.append((x, y + 1, newTravelDistance, "U"))
        queue.append((x, y - 1, newTravelDistance, "D"))

    return None


timeToTitans, height, width = list(map(int, input().split()))
lines = []
grid = []
for y in range(height):
    distances = [-1] * width
    grid.append(distances)
    line = list(input())
    lines.append(line)
    if "S" in line:
        startingX = line.index("S")
        startingY = y

timeToEscape = traverse(lines, grid, startingX, startingY)
if timeToEscape is None or timeToTitans < timeToEscape:
    print("NOT POSSIBLE")
else:
    print(timeToEscape)
