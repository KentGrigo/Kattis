def getNumberOfStars(height, width, lines):
    def helper(xStart, yStart):
        stack = []
        stack.append((xStart, yStart))
        while stack:
            x, y = stack.pop()
            isXWithinBounds = 0 <= x < width
            isYWithinBounds = 0 <= y < height
            if not isXWithinBounds or not isYWithinBounds:
                continue

            entry = lines[y][x]
            if entry != "-":
                continue

            lines[y][x] = "S"
            stack.append((x - 1, y))
            stack.append((x + 1, y))
            stack.append((x, y - 1))
            stack.append((x, y + 1))

    numberOfStars = 0
    for x in range(width):
        for y in range(height):
            entry = lines[y][x]
            if entry == "-":
                numberOfStars += 1
                helper(x, y)

    return numberOfStars


caseNumber = 1
while True:
    try:
        height, width = list(map(int, input().split()))
    except EOFError:
        break

    lines = []
    for _ in range(height):
        line = list(input())
        lines.append(line)

    numberOfStars = getNumberOfStars(height, width, lines)
    print("Case {}: {}".format(caseNumber, numberOfStars))
    caseNumber += 1
