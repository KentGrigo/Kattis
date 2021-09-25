import math

numberOfNeededSquares = int(input())
chocolateSize = 2 ** math.ceil(math.log2(numberOfNeededSquares))

numberOfBreaks = 0
if chocolateSize == numberOfNeededSquares:
    numberOfNeededSquares = 0

brokenChocolateSize = chocolateSize
while 0 < numberOfNeededSquares:
    brokenChocolateSize /= 2
    numberOfBreaks += 1
    if brokenChocolateSize <= numberOfNeededSquares:
        numberOfNeededSquares -= brokenChocolateSize

print("{} {}".format(chocolateSize, numberOfBreaks))
