import math

numberOfStars = int(input())
print("{}:".format(numberOfStars))

def matches(numberOfStarsInFirstRow, numberOfStarsInSecondRow):
    remainder = numberOfStars % (numberOfStarsInFirstRow + numberOfStarsInSecondRow)
    if (remainder == 0 or remainder == numberOfStarsInFirstRow):
        print("{},{}".format(numberOfStarsInFirstRow, numberOfStarsInSecondRow))

half = math.ceil(numberOfStars / 2) + 1
for numberOfStarsInFirstRow in range(2, half):
    matches(numberOfStarsInFirstRow, numberOfStarsInFirstRow - 1)
    matches(numberOfStarsInFirstRow, numberOfStarsInFirstRow)
