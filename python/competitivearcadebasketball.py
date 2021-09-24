numberOfParticipants, numberOfRequiredPoints, numberOfScores = list(map(int, input().split()))
nameToPoints = {}
for _ in range(numberOfParticipants):
    name = input()
    nameToPoints[name] = 0

hasWinners = False
for _ in range(numberOfScores):
    name, points = input().split()
    points = int(points)
    previousPoints = nameToPoints[name]
    nameToPoints[name] += points
    currentPoints = nameToPoints[name]
    if previousPoints < numberOfRequiredPoints <= currentPoints:
        hasWinners = True
        print("{} wins!".format(name))

if not hasWinners:
    print("No winner!")
