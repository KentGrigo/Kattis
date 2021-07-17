import math

numberOfTests = int(input())

for _ in range(numberOfTests):
    encodedMessage = input()
    rowLength = int(math.sqrt(len(encodedMessage)))
    rows = []
    for rowIndex in range(rowLength):
        row = ""
        for columnIndex in range(rowLength):
            index = rowLength * rowIndex + columnIndex
            letter = encodedMessage[index]
            row += letter
        rows.append(row[::-1])

    transposedRows = [*zip(*rows)]
    message = ""
    for row in transposedRows:
        for letter in row:
            message += letter
    print(message)
