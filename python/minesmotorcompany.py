def calculateWorkspaceDistance(previousWorkspace, currentWorkspace):
    verticalDistance = abs(ord(previousWorkspace[0]) - ord(currentWorkspace[0]))
    horizontalDistance = abs(ord(previousWorkspace[1]) - ord(currentWorkspace[1]))
    return verticalDistance + horizontalDistance

numberOfWorkstations = int(input())
previousWorkspace = None
distanceTravelled = 0
for _ in range(numberOfWorkstations):
    currentWorkspace = input()
    if previousWorkspace is not None:
        distance = calculateWorkspaceDistance(previousWorkspace, currentWorkspace)
        distanceTravelled += distance

    previousWorkspace = currentWorkspace

print(distanceTravelled)
