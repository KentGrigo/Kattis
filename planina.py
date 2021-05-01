numberOfIterations = int(input())

numberOfPointsOnSide = 2
for _ in range(numberOfIterations):
    numberOfPointsOnSide += numberOfPointsOnSide - 1

totalNumberOfPoints = numberOfPointsOnSide * numberOfPointsOnSide
print(totalNumberOfPoints)
