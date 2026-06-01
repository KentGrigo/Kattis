numberOfCostumes = int(input())
costumeToCount = {}
for _ in range(numberOfCostumes):
    costume = input()
    if costume not in costumeToCount.keys():
        costumeToCount[costume] = 0

    costumeToCount[costume] += 1

minOccurrence = min(costumeToCount.values())
bestCostumes = sorted([k for k, v in costumeToCount.items() if v == minOccurrence])
for bestCostume in bestCostumes:
    print(bestCostume)
