def getEntry(rows, rowNumber, columnNumber):
    if 0 <= rowNumber < numberOfRows and 0 <= columnNumber < numberOfColumns:
        return rows[rowNumber][columnNumber]
    else:
        return None

def setEntry(rows, rowNumber, columnNumber, newValue):
    if 0 <= rowNumber < numberOfRows and 0 <= columnNumber < numberOfColumns:
        rows[rowNumber][columnNumber] = newValue
    else:
        raise Exception("Not valid coordinates ({}, {}) for {}".format(rowNumber, columnNumber, rows))

def computeNumberOfHandshakes(rows, rowNumber, columnNumber):
    numberOfHandshakes = 0
    for relativeNeighborRowNumber in range(-1, 2):
        for relativeNeighborColumnNumber in range(-1, 2):
            if relativeNeighborRowNumber == 0 and relativeNeighborColumnNumber == 0:
                continue

            neighborRowNumber = rowNumber + relativeNeighborRowNumber
            neighborColumnNumber = columnNumber + relativeNeighborColumnNumber
            neighborEntry = getEntry(rows, neighborRowNumber, neighborColumnNumber)
            if neighborEntry != "o":
                continue

            numberOfHandshakes += 1
    
    return numberOfHandshakes


size = input().split()
numberOfRows = int(size[0])
numberOfColumns = int(size[1])

rows = []
for _ in range(numberOfRows):
    row = list(input())
    rows.append(row)

# Find seat for Mirko
rowNumberOfMirko = None
columnNumberOfMirko = None
maxNumberOfHandshakes = 0
for rowNumber in range(numberOfRows):
    for columnNumber in range(numberOfColumns):
        entry = getEntry(rows, rowNumber, columnNumber)
        if entry != ".":
            continue

        numberOfHandshakes = computeNumberOfHandshakes(rows, rowNumber, columnNumber)
        if maxNumberOfHandshakes < numberOfHandshakes:
            maxNumberOfHandshakes = numberOfHandshakes
            rowNumberOfMirko = rowNumber
            columnNumberOfMirko = columnNumber

if rowNumberOfMirko != None and columnNumberOfMirko != None:
    setEntry(rows, rowNumberOfMirko, columnNumberOfMirko, "o")

# Compute total number of seats
totalNumberOfHandshakes = 0
for rowNumber in range(numberOfRows):
    for columnNumber in range(numberOfColumns):
        entry = getEntry(rows, rowNumber, columnNumber)
        if entry != "o":
            continue

        totalNumberOfHandshakes += computeNumberOfHandshakes(rows, rowNumber, columnNumber)

print(totalNumberOfHandshakes // 2)
