while True:
    numberOfDataPoints = int(input())
    if numberOfDataPoints == -1:
        break

    totalDistance = 0 # miles
    previousTotalTimeElapsed = 0 # hours
    for _ in range(numberOfDataPoints):
        dataPoint = input().split()
        speed = int(dataPoint[0])
        totalTimeElapsed = int(dataPoint[1])

        timeElapsed = totalTimeElapsed - previousTotalTimeElapsed
        previousTotalTimeElapsed = totalTimeElapsed
        totalDistance += speed * timeElapsed

    print("{} miles".format(totalDistance))
