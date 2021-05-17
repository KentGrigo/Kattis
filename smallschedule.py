import math

timeForLongBatches, numberOfMachines, numberOfShortBatches, numberOfLongBatches = list(map(int, input().split()))

numberOfLeftoverLongBatches = numberOfLongBatches % numberOfMachines
numberOfNeededShortBatchesToMatch = timeForLongBatches * (numberOfMachines - numberOfLeftoverLongBatches)
if 0 < numberOfLeftoverLongBatches and numberOfShortBatches < numberOfNeededShortBatchesToMatch:
    totalTimeForLongBatches = timeForLongBatches * int(math.ceil(numberOfLongBatches / numberOfMachines))
    totalTime = totalTimeForLongBatches
else: # numberOfNeededShortBatchesToMatch < numberOfShortBatches:
    timeForAllBatches = timeForLongBatches * numberOfLongBatches + numberOfShortBatches
    totalTime = int(math.ceil(timeForAllBatches / numberOfMachines))

print(totalTime)
