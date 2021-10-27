firstOccurrence = None
numberOfPairs = int(input())
for _ in range(numberOfPairs):
    lastSeen, cycle1, cycle2 = list(map(int, input().split()))
    nextYear1 = lastSeen + cycle1
    nextYear2 = lastSeen + cycle2
    while nextYear1 != nextYear2:
        if nextYear1 < nextYear2:
            nextYear1 = nextYear1 + cycle1
        else:
            nextYear2 = nextYear2 + cycle2

    nextSeen = nextYear1
    if firstOccurrence is None or nextSeen < firstOccurrence:
        firstOccurrence = nextSeen

print(firstOccurrence)
