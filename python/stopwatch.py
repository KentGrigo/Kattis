numberOfPresses = int(input())
isRunning = False
accumulatedTime = 0
previousTime = 0
for _ in range(numberOfPresses):
    currentTime = int(input())
    if isRunning:
        accumulatedTime += currentTime - previousTime

    previousTime = currentTime
    isRunning = not isRunning

if isRunning:
    print("still running")
else:
    print(accumulatedTime)
