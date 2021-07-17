numberOfCases = int(input())
for _ in range(numberOfCases):
    data = input().split()
    caseNumber = int(data[0])
    numberOfDays = int(data[1])

    totalNumberOfCandles = 0
    for numberOfMenorahCandles in range(1, numberOfDays + 1):
        totalNumberOfCandles += numberOfMenorahCandles + 1

    print("{} {}".format(caseNumber, totalNumberOfCandles))
