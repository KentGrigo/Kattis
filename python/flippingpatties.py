import math

def incrementEntry(time):
    timeToNumberOfActions[time] = 1 + timeToNumberOfActions.get(time, 0)


numberOfOrders = int(input())
timeToNumberOfActions = {}
for _ in range(numberOfOrders):
    timeToCook, timeToServe = list(map(int, input().split()))
    incrementEntry(timeToServe - timeToCook * 2)
    incrementEntry(timeToServe - timeToCook)
    incrementEntry(timeToServe)

maxNumberOfHandsNeeded = max(timeToNumberOfActions.values())
maxNumberOfCooksNeeded = int(math.ceil(maxNumberOfHandsNeeded / 2))
print(maxNumberOfCooksNeeded)
