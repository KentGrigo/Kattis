import math

numberOfTargets = int(input())
rectangles = []
circles = []
for _ in range(numberOfTargets):
    type, *dimensions = input().split()
    dimensions = list(map(int, dimensions))
    if type == "rectangle":
        rectangles.append(dimensions)
    else:
        circles.append(dimensions)

numberOfShots = int(input())
for _ in range(numberOfShots):
    x, y = list(map(int, input().split()))
    numberOfHits = 0
    for x1, y1, x2, y2 in rectangles:
        if x1 <= x <= x2 and y1 <= y <= y2:
            numberOfHits += 1

    for x1, y1, radius in circles:
        diffX = x1 - x
        diffY = y1 - y
        distance = math.sqrt(diffX ** 2 + diffY ** 2)
        if distance <= radius:
            numberOfHits += 1

    print(numberOfHits)
