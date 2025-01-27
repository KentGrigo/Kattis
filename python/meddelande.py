numberOfRows, numberOfColumns = list(map(int, input().split()))
rows = []
for _ in range(numberOfRows):
    row = input()
    rows.append(row)

x = 0
y = 0
message = ""
if rows[y][x] != '.':
    message += rows[y][x]

while x != numberOfColumns - 1 or y != numberOfRows - 1:
    foundLetter = False
    for newX in range(x + 1, numberOfColumns):
        cell = rows[y][newX]
        if cell != '.':
            message += cell
            x = newX
            foundLetter = True

    for newY in range(y + 1, numberOfRows):
        cell = rows[newY][x]
        if cell != '.':
            message += cell
            y = newY
            foundLetter = True

    if not foundLetter:
        y = min(y + 1, numberOfRows - 1)

print(message)
