def isFieldCovered(fieldSize, halfWidth, startingPositions):
    covered = 0.0
    for startingPosition in startingPositions:
        if startingPosition - halfWidth <= covered:
            covered = startingPosition + halfWidth
        else:
            return False

    return fieldSize <= covered


stadiumLength = 100
stadiumWidth = 75

while True:
    data = input().split()
    numberOfVerticalStartingPositions = int(data[0])
    numberOfHorizontalStartingPositions = int(data[1])
    width = float(data[2])

    if numberOfVerticalStartingPositions == 0 and \
        numberOfHorizontalStartingPositions == 0 and \
        width == 0.0:
        break

    verticalStartingPositions = list(map(float, input().split()))
    horizontalStartingPositions = list(map(float, input().split()))

    verticalStartingPositions.sort()
    horizontalStartingPositions.sort()

    halfWidth = width / 2
    isFieldCoveredVertically = isFieldCovered(stadiumWidth, halfWidth, verticalStartingPositions)
    isFieldCoveredHorizontally = isFieldCovered(stadiumLength, halfWidth, horizontalStartingPositions)

    if isFieldCoveredVertically and isFieldCoveredHorizontally:
        print("YES")
    else:
        print("NO")
