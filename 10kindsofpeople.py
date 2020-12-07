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

def normalizeMap(map, positions, fieldType, newFieldValue):
    while len(positions) != 0:
        position = positions.pop()
        x = position[0]
        y = position[1]
        field = get(map, x, y)
        if field != fieldType:
            continue

        set(map, x, y, newFieldValue)
        positions.append((x-1, y))
        positions.append((x+1, y))
        positions.append((x, y-1))
        positions.append((x, y+1))
        
def normalize(map):
    groupNumber = 0
    for y in range(height):
        for x in range(width):
            field = get(map, x, y)
            if field == "0" or field == "1":
                groupNumber += 1
                normalizeMap(map, [(x, y)], field, groupNumber)
    return map


mapSize = input().split()
height = int(mapSize[0])
width = int(mapSize[1])

originalMap = []
normalizedMap = []
for _ in range(height):
    originalRow = list(input())
    originalMap.append(originalRow)
    normalizedRow = originalRow.copy()
    normalizedMap.append(normalizedRow)

normalize(normalizedMap)

numberOfQueries = int(input())
for _ in range(numberOfQueries):
    query = input().split()
    y1 = int(query[0]) - 1
    x1 = int(query[1]) - 1
    y2 = int(query[2]) - 1
    x2 = int(query[3]) - 1
    fieldType = get(originalMap, x1, y1)
    field1 = get(normalizedMap, x1, y1)
    field2 = get(normalizedMap, x2, y2)
    if field1 == field2:
        if fieldType == "0":
            print("binary")
        else:
            print("decimal")
    else:
        print("neither")
