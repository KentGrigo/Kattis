numberOfMachines, numberOfItems = list(map(int, input().split()))
processingTimes = list(map(int, input().split()))
inputTapes = list(map(int, input().split()))

totalProcessingTime = sum(processingTimes) + (numberOfItems - 1) * max(processingTimes)
print(totalProcessingTime)
