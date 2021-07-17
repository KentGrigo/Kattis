caseNumber = 0
while True:
    try:
        numberOfNumbers = int(input())
    except EOFError:
        break

    caseNumber += 1
    print("Case {}:".format(caseNumber))

    numbers = []
    for _ in range(numberOfNumbers):
        number = int(input())
        numbers.append(number)

    sums = []
    for index, number1 in enumerate(numbers):
        for number2 in numbers[index+1:]:
            sum = number1 + number2
            sums.append(sum)

    numberOfQueries = int(input())
    for _ in range(numberOfQueries):
        query = int(input())
        closestSum = sums[0]
        minDifference = abs(query - closestSum)
        for sum in sums:
            difference = abs(query - sum)
            if difference < minDifference:
                minDifference = difference
                closestSum = sum

        print("Closest sum to {} is {}.".format(query, closestSum))
