numberOfUsers, minimumUserCount = list(map(int, input().split()))

hourToNumberOfUsers = {}
for hour in range(24):
    hourToNumberOfUsers[hour] = 0

for _ in range(numberOfUsers):
    start, end = list(map(int, input().split()))
    for hour in range(start, end):
        hourToNumberOfUsers[hour] += 1

numberOfHoursAboveLimit = 0
for hour in range(24):
    numberOfUsers = hourToNumberOfUsers[hour]
    if minimumUserCount <= numberOfUsers:
        numberOfHoursAboveLimit += 1

print(numberOfHoursAboveLimit)
