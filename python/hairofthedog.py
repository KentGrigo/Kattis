numberOfDays = int(input())
numberOfDaysWithHangover = 0
previousCondition = "sober"
for _ in range(numberOfDays):
    currentCondition = input()
    if previousCondition == "drunk" and currentCondition == "sober":
        numberOfDaysWithHangover += 1

    previousCondition = currentCondition

print(numberOfDaysWithHangover)
