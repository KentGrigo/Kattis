def isWithinBounds(x, y):
    return 0 <= x < width and 0 <= y < height


height, width = list(map(int, input().split()))
rows = []
for _ in range(height):
    row = list(input())
    rows.append(row)

x = 0
y = 0
numberOfSteps = 0
while True:
    if not isWithinBounds(x, y):
        print("Out")
        break

    element = rows[y][x]
    if element == "T":
        print(numberOfSteps)
        break
    elif element == "X":
        print("Lost")
        break

    rows[y][x] = "X"
    if element == "N":
        y -= 1
    elif element == "S":
        y += 1
    elif element == "E":
        x += 1
    elif element == "W":
        x -= 1

    numberOfSteps += 1
