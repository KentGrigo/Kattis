from collections import deque

def get(cells, rowIndex, columnIndex):
    if 0 <= rowIndex < numberOfRows and 0 <= columnIndex < numberOfColumns:
        return cells[rowIndex][columnIndex]
    else:
        return None

def set(cells, rowIndex, columnIndex, newvalue):
    if 0 <= rowIndex < numberOfRows and 0 <= columnIndex < numberOfColumns:
        cells[rowIndex][columnIndex] = newvalue
    else:
        raise ValueError(
            """The index of the row or the column was out of bounds. 
            The row index {} must be within [0; {}[, and 
            the column index {} must be within [0;{}[."""
            .format(rowIndex, numberOfRows, columnIndex, numberOfColumns)
        )


data = input().split()
numberOfRows = int(data[0])
numberOfColumns = int(data[1])
numberOfInitialCells = int(data[2])

maxValue = numberOfRows * numberOfColumns + 1
cells = []
for _ in range(numberOfRows):
    row = []
    for _ in range(numberOfColumns):
        entry = maxValue
        row.append(entry)
    
    cells.append(row)

fieldsToVisit = deque()
for _ in range(numberOfInitialCells):
    coordinate = map(lambda value: int(value) - 1, input().split())
    fieldsToVisit.append((coordinate, 1))

while fieldsToVisit:
    (rowIndex, columnIndex), value = fieldsToVisit.popleft()
    currentValue = get(cells, rowIndex, columnIndex)
    if currentValue != None and value < currentValue:
        set(cells, rowIndex, columnIndex, value)
        fieldsToVisit.append(((rowIndex - 1, columnIndex), value + 1))
        fieldsToVisit.append(((rowIndex + 1, columnIndex), value + 1))
        fieldsToVisit.append(((rowIndex, columnIndex - 1), value + 1))
        fieldsToVisit.append(((rowIndex, columnIndex + 1), value + 1))

numberOfDaysToConquer = 0
for row in cells:
    for value in row:
        numberOfDaysToConquer = max(value, numberOfDaysToConquer)

print(numberOfDaysToConquer)
