height, width, racketSize = list(map(int, input().split()))
rows = []
for _ in range(height):
    row = list(input())
    rows.append(row)

bestStartX = 0
bestStartY = 0
maxNumberOfFlies = 0
for startY in range(height - racketSize + 1):
    for startX in range(width - racketSize + 1):
        numberOfFlies = 0
        for y in range(startY + 1, startY + racketSize - 1):
            for x in range(startX + 1, startX + racketSize - 1):
                cell = rows[y][x]
                if cell == "*":
                    numberOfFlies += 1

        if maxNumberOfFlies < numberOfFlies:
            bestStartX = startX
            bestStartY = startY
            maxNumberOfFlies = numberOfFlies

print(maxNumberOfFlies)
rows[bestStartY][bestStartX] = "+"
rows[bestStartY + racketSize - 1][bestStartX] = "+"
rows[bestStartY][bestStartX + racketSize - 1] = "+"
rows[bestStartY + racketSize - 1][bestStartX + racketSize - 1] = "+"
for y in range(bestStartY + 1, bestStartY + racketSize - 1):
    rows[y][bestStartX] = "|"
    rows[y][bestStartX + racketSize - 1] = "|"

for x in range(bestStartX + 1, bestStartX + racketSize - 1):
    rows[bestStartY][x] = "-"
    rows[bestStartY + racketSize - 1][x] = "-"

for row in rows:
    print("".join(row))
