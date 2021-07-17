def test(values):
    sortedValues = sorted(values)
    sortedIndex = 0
    numberOfActions = 0
    for value in values:
        sortedValue = sortedValues[sortedIndex]
        if value == sortedValue:
            sortedIndex += 1
        else:
            numberOfActions += 1

    return numberOfActions


numberOfTests = int(input())
for _ in range(numberOfTests):
    testNumber, amountOfData = list(map(int, input().split()))

    values = []
    while 0 < amountOfData:
        data = list(map(int, input().split()))
        values.extend(data)
        amountOfData -= 10

    result = test(values)
    print("{} {}".format(testNumber, result))
