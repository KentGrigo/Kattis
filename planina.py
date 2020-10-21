numberOfIterations = int(input())

numberOfPointsOnSide = 2
for i in range(numberOfIterations):
    numberOfPointsOnSide += numberOfPointsOnSide - 1
    
totalNumberOfPoints = numberOfPointsOnSide * numberOfPointsOnSide
print(totalNumberOfPoints)