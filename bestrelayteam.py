numberOfRunners = int(input())
firstLapScores = []
restLapScores = []
for _ in range(numberOfRunners):
    data = input().split()
    name = data[0]
    firstLapTime = float(data[1])
    restLapTime = float(data[2])
    firstLapScores.append((firstLapTime, name))
    restLapScores.append((restLapTime, name))

firstLapScores.sort()
restLapScores.sort()

numberOfLegs = 4
maxTime = 20
bestTime = numberOfLegs * maxTime
bestTeamNames = None
for (firstRunnerTime, firstRunnerName) in firstLapScores[0:numberOfLegs]:
    bestRestRunners = list(filter(lambda restScore: restScore[1] != firstRunnerName, restLapScores))[0:numberOfLegs-1]
    teamTime = firstRunnerTime
    teamNames = [firstRunnerName]
    for (restRunnerTime, restRunnerName) in bestRestRunners:
        teamTime += restRunnerTime
        teamNames.append(restRunnerName)

    if teamTime < bestTime:
        bestTime = teamTime
        bestTeamNames = teamNames

print(bestTime)
for bestTeamName in bestTeamNames:
    print(bestTeamName)
