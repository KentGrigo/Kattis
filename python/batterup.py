input()
data = input().split()
bases = map(lambda value: int(value), data)

numberOfAtBats = 0
numberOfBases = 0
for base in bases:
    if (base == -1):
        continue
    else:
        numberOfAtBats += 1
        numberOfBases += base

average = numberOfBases / numberOfAtBats
print(average)