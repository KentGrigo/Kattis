data = input().split()
startTime = int(data[0])
endTime = int(data[1])
numberOfBuses = int(data[2])

walkingTimes = list(map(lambda walkingTime: int(walkingTime), input().split()))
busTimes = list(map(lambda busTime: int(busTime), input().split()))
busArrivalFrequencies = list(map(lambda busArrivalFrequency: int(busArrivalFrequency), input().split()))

currentTime = startTime

for busNumber in range(numberOfBuses):
    walkingTime = walkingTimes[busNumber]
    currentTime += walkingTime # walk to the bus

    timeTooLate = currentTime % busArrivalFrequencies[busNumber]
    waitingTime = 0 if timeTooLate == 0 else busArrivalFrequencies[busNumber] - timeTooLate
    currentTime += waitingTime # wait for the bus

    busTime = busTimes[busNumber]
    currentTime += busTime # take the bus

currentTime += walkingTimes[-1] # walk to school

if currentTime <= endTime:
    print("yes")
else:
    print("no")