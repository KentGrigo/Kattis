caseNumber = 0
while True:
    caseNumber += 1
    try:
        amountOfData, *data = list(map(int, input().split()))
    except EOFError:
        break

    minimum = min(data)
    maximum = max(data)
    difference = maximum - minimum
    print("Case {}: {} {} {}".format(caseNumber, minimum, maximum, difference))
