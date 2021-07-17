numberOfSocks, maxCapacity, maxColorDifference = list(map(int, input().split()))
sockColors = list(map(int, input().split()))
sockColors.sort()

numberOfMachines = 0
startSockColor = sockColors[0]
numberOfSocksForMachine = maxCapacity
for sockColor in sockColors:
    needsNewMachine = maxCapacity <= numberOfSocksForMachine or \
                        maxColorDifference < sockColor - startSockColor
    if needsNewMachine:
        numberOfMachines += 1
        startSockColor = sockColor
        numberOfSocksForMachine = 0

    numberOfSocksForMachine += 1

print(numberOfMachines)
