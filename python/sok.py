amountOfJuices = list(map(int, input().split()))
juiceRatios = list(map(int, input().split()))

minDosis = None
for amountOfJuice, juiceRatio in zip(amountOfJuices, juiceRatios):
    dosis = amountOfJuice / juiceRatio
    if minDosis is None or dosis < minDosis:
        minDosis = dosis

leftovers = []
for amountOfJuice, juiceRatio in zip(amountOfJuices, juiceRatios):
    juiceUsed = juiceRatio * minDosis
    leftover = amountOfJuice - juiceUsed
    leftovers.append(leftover)

print(" ".join(map(str, leftovers)))
