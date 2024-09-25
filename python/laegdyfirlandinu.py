def hasLowPressure(rows):
    for rowIndex in range(1, numberOfRows - 1):
        for columnIndex in range(1, numberOfColumns - 1):
            cell = rows[rowIndex][columnIndex]
            left = rows[rowIndex - 1][columnIndex]
            right = rows[rowIndex + 1][columnIndex]
            up = rows[rowIndex][columnIndex - 1]
            down = rows[rowIndex][columnIndex + 1]
            if cell < left and cell < right and cell < up and cell < down:
                return True

    return False

numberOfRows, numberOfColumns = list(map(int, input().split()))
rows = []
for _ in range(numberOfRows):
    row = list(map(int, input().split()))
    rows.append(row)

if hasLowPressure(rows):
    print("Jebb")
else:
    print("Neibb")
