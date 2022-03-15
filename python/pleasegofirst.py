from collections import Counter

def getGroupToLastIndex(queue):
    groupToLastIndex = {}
    for index, group in reversed(list(zip(range(numberOfPeople), queue))):
        if group not in groupToLastIndex:
            groupToLastIndex[group] = index

    return groupToLastIndex

def computeWaitingTime(queue):
    groupToLastIndex = getGroupToLastIndex(queue)
    waitingTime = 0
    for index, person in enumerate(queue):
        lastIndex = groupToLastIndex[person]
        difference = 5 * (lastIndex - index)
        waitingTime += difference

    return waitingTime


numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfPeople = int(input())
    queue = list(input())

    groupSizes = Counter(queue)
    orderedGroups = list(queue)
    orderedGroups.reverse()
    orderedGroups = list(dict.fromkeys(orderedGroups))
    orderedGroups.reverse()
    rearrangedQueue = []
    for group in orderedGroups:
        groupSize = groupSizes[group]
        for _ in range(groupSize):
            rearrangedQueue.append(group)

    waitingTime = computeWaitingTime(queue)
    newWaitingTime = computeWaitingTime(rearrangedQueue)
    savedWaitingTime = waitingTime - newWaitingTime
    print(savedWaitingTime)
