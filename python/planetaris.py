numberOfSolarSystems, fleetSize = list(map(int, (input().split())))
enemyFleetSizes = sorted(map(int, input().split()))
numberOfVictories = 0
for enemyFleetSize in enemyFleetSizes:
    fleetSize -= (enemyFleetSize + 1)
    if 0 <= fleetSize:
        numberOfVictories += 1

print(numberOfVictories)
