numberOfTeams, numberOfDamages, numberOfReserves = list(map(int, input().split()))
damages = sorted(map(int, input().split()))
reserves = sorted(map(int, input().split()))

numberOfDisqualifiedTeams = 0
damageIndex = 0
reserveIndex = 0
while damageIndex < numberOfDamages and reserveIndex < numberOfReserves:
    damage = damages[damageIndex]
    reserve = reserves[reserveIndex]
    if reserve + 1 < damage:
        reserveIndex += 1
    elif damage < reserve - 1:
        damageIndex += 1
        numberOfDisqualifiedTeams += 1
    else:
        damageIndex += 1
        reserveIndex += 1

numberOfDisqualifiedTeams += (numberOfDamages - damageIndex)
print(numberOfDisqualifiedTeams)
