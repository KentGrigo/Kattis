numberOfNumbers = int(input())
numbers = list(map(int, input().split()))

biggestBefore = []
biggestSoFar = float("-inf")
for number in numbers:
    biggestSoFar = max(number, biggestSoFar)
    biggestBefore.append(biggestSoFar)

smallestAfter = []
smallestSoFar = float("inf")
for number in reversed(numbers):
    smallestSoFar = min(number, smallestSoFar)
    smallestAfter.append(smallestSoFar)

smallestAfter = list(reversed(smallestAfter))

numberOfPivots = 0
for index, number in enumerate(numbers):
    biggestNumberBefore = biggestBefore[index]
    smallestNumberAfter = smallestAfter[index]
    isPivot = biggestNumberBefore <= number and number <= smallestNumberAfter
    if isPivot:
        numberOfPivots += 1

print(numberOfPivots)
