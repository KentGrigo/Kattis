import math

numberOfOrderedPizzas = int(input())
sizeToNumberOfPizzas = {
    'S': 0,
    'M': 0,
    'L': 0,
}
for _ in range(numberOfOrderedPizzas):
    size, numberOfLeftovers = input().split()
    numberOfLeftovers = int(numberOfLeftovers)
    sizeToNumberOfPizzas[size] += numberOfLeftovers

numberOfLeftoverBoxes = \
    math.ceil(sizeToNumberOfPizzas['S'] / 6) \
    + math.ceil(sizeToNumberOfPizzas['M'] / 8) \
    + math.ceil(sizeToNumberOfPizzas['L'] / 12)
print(numberOfLeftoverBoxes)
