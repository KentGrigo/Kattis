data = input().split()
numberOfOwnedEmptyBottles = int(data[0])
numberOfFoundEmptyBottles = int(data[1])
numberOfRequiredEmptyBottles = int(data[2])

totalBottles = 0
numberOfEmptyBottles = numberOfOwnedEmptyBottles + numberOfFoundEmptyBottles
while numberOfRequiredEmptyBottles <= numberOfEmptyBottles:
    leftover = numberOfEmptyBottles % numberOfRequiredEmptyBottles
    newBottles = numberOfEmptyBottles // numberOfRequiredEmptyBottles
    totalBottles += newBottles
    numberOfEmptyBottles = leftover + newBottles

print(totalBottles)
