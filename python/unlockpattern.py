from math import sqrt

lockSize = 3
orderToPosition = {}
for rowNumber in range(lockSize):
    for columnNumber, order in enumerate(map(int, input().split())):
        orderToPosition[order] = (columnNumber, rowNumber)

totalDistance = 0
for previousPivot in range(1, lockSize ** 2):
    currentPivot = previousPivot + 1
    previousPosition = orderToPosition[previousPivot]
    currentPosition = orderToPosition[currentPivot]
    diffX = currentPosition[0] - previousPosition[0]
    diffY = currentPosition[1] - previousPosition[1]
    distance = sqrt(diffX ** 2 + diffY ** 2)
    totalDistance += distance

print(totalDistance)
