numberOfTests = int(input())
for _ in range(numberOfTests):
    dataSetNumber, limit = list(map(int, input().split()))

    totalSum = 0
    for value in range(0, limit + 1):
        totalSum += value

    evenSum = 0
    for value in range(0, limit * 2 + 1, 2):
        evenSum += value

    oddSum = 0
    for value in range(1, limit * 2 + 1, 2):
        oddSum += value

    print("{} {} {} {}".format(dataSetNumber, totalSum, oddSum, evenSum))
