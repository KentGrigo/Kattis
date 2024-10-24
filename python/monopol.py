numberOfHotels = int(input())
hotelPositions = list(map(int, input().split()))

numberOfCombinations = 0
sumToHitRate = {}
for die1 in range(1, 7):
    for die2 in range(1, 7):
        numberOfCombinations += 1
        sum = die1 + die2
        newHitRate = sumToHitRate.get(sum, 0) + 1
        sumToHitRate[sum] = newHitRate

accumulatedHitRates = 0
for hotelPosition in hotelPositions:
    hitRate = sumToHitRate[hotelPosition]
    accumulatedHitRates += hitRate

probability = accumulatedHitRates / numberOfCombinations
print(probability)
