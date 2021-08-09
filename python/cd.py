from sys import stdin

while True:
    numberOfCdsJack, numberOfCdsJill = list(map(int, stdin.readline().split()))
    if numberOfCdsJack == 0 and numberOfCdsJill == 0:
        break

    catalogNumberToOwnership = {}
    for _ in range(numberOfCdsJack):
        catalogNumber = int(stdin.readline())
        catalogNumberToOwnership[catalogNumber] = True

    numberOfDuplicateCds = 0
    for _ in range(numberOfCdsJill):
        catalogNumber = int(stdin.readline())
        if catalogNumber in catalogNumberToOwnership:
            numberOfDuplicateCds += 1

    print(numberOfDuplicateCds)
