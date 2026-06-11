import math

def computerTime(numberOfDigits):
    return numberOfDigits * math.log10(numberOfDigits) / 10 ** 6


timeInSeconds = int(input())
lowerBound = 0
upperBound = 189481 * timeInSeconds
while lowerBound + 1 < upperBound:
    estimate = int(lowerBound + (upperBound - lowerBound) / 2)
    actualTimeInSeconds = computerTime(estimate)
    if timeInSeconds < actualTimeInSeconds:
        upperBound = estimate
    else:
        lowerBound = estimate

if computerTime(upperBound) < timeInSeconds:
    print(upperBound)
else:
    print(lowerBound)
