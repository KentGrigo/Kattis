numberOfSeedlings = int(input())
seedlings = list(map(int, input().split()))
seedlings.sort()

seedlingTimeLeft = 0
numberOfDays = 0
for seedling in reversed(seedlings):
    numberOfDays += 1
    seedlingTimeLeft -= 1
    seedlingTimeLeft = max(seedlingTimeLeft, seedling)

timeToParty = numberOfDays + seedlingTimeLeft + 1
print(timeToParty)
