numberOfDaysInWeek = 7
numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfFridayThe13th = 0
    totalNumberOfDays, numberOfMonths = list(map(int, input().split()))
    numberOfDaysInMonths = list(map(int, input().split()))
    weekdayOfThe1st = 2 # Friday is 0, Sunday is 2. The year always starts on a Sunday.
    for numberOfDaysInMonth in numberOfDaysInMonths:
        if 13 <= numberOfDaysInMonth:
            weekdayOfThe13th = (weekdayOfThe1st + 12) % numberOfDaysInWeek
            if weekdayOfThe13th == 0:
                numberOfFridayThe13th += 1

        weekdayOfThe1st = (weekdayOfThe1st + numberOfDaysInMonth) % numberOfDaysInWeek

    print(numberOfFridayThe13th)
