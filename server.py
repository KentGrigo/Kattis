numberOfTasks, serverTime = list(map(int, input().split()))
taskTimes = list(map(int, input().split()))
numberOfRunnableTasks = 0
accumulatedTime = 0
for taskTime in taskTimes:
    accumulatedTime += taskTime
    if accumulatedTime <= serverTime:
        numberOfRunnableTasks += 1
    else:
        break

print(numberOfRunnableTasks)
