numberOfTasks, numberOfQuietIntervals = list(map(int, input().split()))
taskDurations = list(map(int, input().split()))
quietIntervalDurations = list(map(int, input().split()))

taskDurations.sort(key = lambda duration: -duration)
quietIntervalDurations.sort(key = lambda duration: -duration)

numberOfFinishedTasks = 0
quietIntervalIndex = 0
for taskDuration in taskDurations:
    if numberOfQuietIntervals <= quietIntervalIndex:
        break

    quietIntervalDuration = quietIntervalDurations[quietIntervalIndex]
    if taskDuration <= quietIntervalDuration:
        numberOfFinishedTasks += 1
        quietIntervalIndex += 1

print(numberOfFinishedTasks)
