numberOfCellsPerLane = int(input())
numberOfLanes = int(input())
numberOfCells = numberOfCellsPerLane * numberOfLanes
emptyCell = "."

numberOfEmptyCells = 0
for _ in range(numberOfLanes):
    lane = input()
    for cell in lane:
        if cell == emptyCell:
            numberOfEmptyCells += 1

proportionOfEmptyCells = numberOfEmptyCells / numberOfCells
print(proportionOfEmptyCells)
