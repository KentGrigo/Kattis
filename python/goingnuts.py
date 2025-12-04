import math

numberOfNuts = int(input())
numberOfSquirrels = 0
while 0 < numberOfNuts:
    nutCollectionSize = 2 ** math.floor(math.log(numberOfNuts, 2))
    numberOfNuts -= nutCollectionSize
    numberOfSquirrels += 1

print(numberOfSquirrels)
