graph = []
numberOfVillages = int(input())
for _ in range(numberOfVillages):
    distances = list(map(lambda distance: int(distance), input().split()))
    graph.append(distances)

maxValue = 10 ** 7
mst = []
key = []
mstSet = []
for _ in range(numberOfVillages):
    mst.append(-1)
    key.append(maxValue)
    mstSet.append(False)

key[0] = 0
for _ in range(numberOfVillages - 1):
    minimum = maxValue
    minimumIndex = -1

    for villageIndex in range(numberOfVillages):
        if mstSet[villageIndex] == False and key[villageIndex] < minimum:
            minimum = key[villageIndex]
            minimumIndex = villageIndex

    mstSet[minimumIndex] = True
    for villageIndex in range(numberOfVillages):
        isAnotherVillage = minimumIndex != villageIndex
        isNotConnectedYet = mstSet[villageIndex] == False
        isShorterPath = graph[minimumIndex][villageIndex] < key[villageIndex]
        if isAnotherVillage and isNotConnectedYet and isShorterPath:
            mst[villageIndex] = minimumIndex
            key[villageIndex] = graph[minimumIndex][villageIndex]

result = []
for villageIndex1, villageIndex2 in enumerate(mst[1:], 1):
    minimumVillageNumber = min(villageIndex1, villageIndex2)
    maximumVillageNumber = max(villageIndex1, villageIndex2)
    result.append((minimumVillageNumber + 1, maximumVillageNumber + 1))

result.sort()
for villageNumber1, villageNumber2 in result:
    print("{} {}".format(villageNumber1, villageNumber2))
