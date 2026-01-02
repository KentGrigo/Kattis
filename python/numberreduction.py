import math

numberOfItems = int(input())
numberOfSteps = 0
while numberOfItems != 1:
    numberOfSteps += 1
    if numberOfItems % 2 == 0:
        numberOfItems = math.floor(numberOfItems / 2)
    else:
        numberOfItems += numberOfItems * 2 + 1

print(numberOfSteps)
