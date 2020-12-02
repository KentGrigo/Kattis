mapSize = input().split()
height = int(mapSize[0])
width = int(mapSize[1])

map = []
for _ in range(height):
    row = list(input())
    map.append(row)

def isWithinBounds(map, x, y):
    return 0 <= x and x < width and 0 <= y and y < height

def get(map, x, y):
    if isWithinBounds(map, x, y):
        return map[y][x]
    else:
        return None

def set(map, x, y, value):
    if isWithinBounds(map, x, y):
        map[y][x] = value

def normalizeLand(map, x, y, newFieldValue):
    field = get(map, x, y)
    if field != "C" and field != "L":
        return

    set(map, x, y, newFieldValue)
    normalizeLand(map, x-1, y, newFieldValue)
    normalizeLand(map, x+1, y, newFieldValue)
    normalizeLand(map, x, y-1, newFieldValue)
    normalizeLand(map, x, y+1, newFieldValue)

def normalize(map):
    islandNumber = 0
    for y in range(height):
        for x in range(width):
            field = get(map, x, y)
            if field == "L":
                islandNumber += 1
                normalizeLand(map, x, y, islandNumber)

    print(islandNumber)

normalize(map)
