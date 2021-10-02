numberOfDirtyDays = int(input())
dirtyDays = list(map(int, input().split()))

dirtiness = 0
numberOfDirtyDaysSinceCleanup = 0
numberOfCleanups = 0
previousDirtyDay = 0
for dirtyDay in dirtyDays:
    dirtiness += numberOfDirtyDaysSinceCleanup * (dirtyDay - previousDirtyDay)
    if 20 <= dirtiness:
        numberOfDirtyDaysSinceCleanup = 0
        numberOfCleanups += 1
        dirtiness = 0

    numberOfDirtyDaysSinceCleanup += 1
    previousDirtyDay = dirtyDay

if 0 < numberOfDirtyDaysSinceCleanup:
    numberOfCleanups += 1

print(numberOfCleanups)
