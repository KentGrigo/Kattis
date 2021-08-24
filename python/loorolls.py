rollLength, needLength = list(map(int, input().split()))
numberOfRolls = 1
while True:
    remainder = rollLength % needLength
    if remainder == 0:
        break

    numberOfRolls += 1
    needLength = needLength - remainder

print(numberOfRolls)
