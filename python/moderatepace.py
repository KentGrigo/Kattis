numberOfTrainingDays = int(input())
personalDailyDistances = list(map(int, input().split()))
firstColleagueDailyDistances = list(map(int, input().split()))
secondColleagueDailyDistances = list(map(int, input().split()))

targetDailyDistances = []
for personalDailyDistance, firstColleagueDailyDistance, secondColleagueDailyDistance in zip(personalDailyDistances, firstColleagueDailyDistances, secondColleagueDailyDistances):
    minLimit = min(firstColleagueDailyDistance, secondColleagueDailyDistance)
    maxLimit = max(firstColleagueDailyDistance, secondColleagueDailyDistance)
    if minLimit <= personalDailyDistance <= maxLimit:
        targetDailyDistances.append(personalDailyDistance)
    elif personalDailyDistance < minLimit:
        targetDailyDistances.append(minLimit)
    else:
        targetDailyDistances.append(maxLimit)

result = " ".join(map(str, targetDailyDistances))
print(result)
