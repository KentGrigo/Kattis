def computeBattleOutcome(battle):
    previousAbility = None
    for currentAbility in battle:
        if previousAbility == "C" and currentAbility == "D":
            return False

        previousAbility = currentAbility

    return True


numberOfWonBattles = 0
numberOfBattles = int(input())
for _ in range(numberOfBattles):
    battle = input()
    result = computeBattleOutcome(battle)
    if result:
        numberOfWonBattles += 1

print(numberOfWonBattles)
