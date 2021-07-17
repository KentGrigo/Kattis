lengthOfSleepingPattern, sleepDuration, sleepNeeded = list(map(int, input().split()))
sleepingPattern = list(input())

numberOfTiredMoments = 0
amountOfSleep = 0
for moment in range(-sleepDuration + 1, 0 + 1):
    isSleeping = "Z" == sleepingPattern[moment]
    if isSleeping:
        amountOfSleep += 1

if amountOfSleep < sleepNeeded:
    numberOfTiredMoments += 1

for moment in range(1, lengthOfSleepingPattern):
    momentThen = moment - sleepDuration
    isSleeping = "Z" == sleepingPattern[moment]
    wasSleeping = "Z" == sleepingPattern[momentThen]
    if isSleeping:
        amountOfSleep += 1

    if wasSleeping:
        amountOfSleep -= 1

    if amountOfSleep < sleepNeeded:
        numberOfTiredMoments += 1

print(numberOfTiredMoments)
