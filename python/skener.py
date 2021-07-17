numberOfRows, numberOfColumns, rowZoom, columnZoom = list(map(int, input().split()))

rows = []
for _ in range(numberOfRows):
    row = list(input())
    rows.append(row)

newRows = []
for row in rows:
    newRow = []
    for letter in row:
        for _ in range(columnZoom):
            newRow.append(letter)

    for _ in range(rowZoom):
        newRows.append(newRow)

for row in newRows:
    print("".join(row))
