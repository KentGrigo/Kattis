def computeNumberOfBeneficiary(numberOfScores, sortedPoints):
    previousPoints = 1001 # max points + 1
    foundDuplicates = False
    for index, point in enumerate(sortedPoints):
        if previousPoints == point:
            foundDuplicates = True
        elif foundDuplicates and previousPoints != point:
            return numberOfScores - index

        previousPoints = point

    return 0


numberOfDataSets = int(input())
for _ in range(numberOfDataSets):
    numberOfScores, *points = list(map(int, input().split()))
    sortedPoints = sorted(points, reverse=True)
    numberOfBeneficiary = computeNumberOfBeneficiary(numberOfScores, sortedPoints)
    print(numberOfBeneficiary)
