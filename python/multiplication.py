while True:
    data = input().split()
    value1 = data[0]
    value2 = data[1]
    operand1 = int(value1)
    operand2 = int(value2)
    if operand1 == 0 and operand2 == 0:
        break

    firstLine = "+---"
    secondLine = "|   "
    thirdLine = "| +"
    for digit in value1:
        firstLine += "----"
        secondLine += "{}   ".format(digit)
        thirdLine += "---+"

    firstLine += "+"
    secondLine += "|"
    thirdLine += " |"
    print(firstLine)
    print(secondLine)
    print(thirdLine)
    

    result = "{}".format(operand1 * operand2)
    operandLength = len(value1 + value2)
    paddingLength = operandLength - len(result)
    paddedResult = paddingLength * " " + result
    hadResultDigit = False
    for digit2, paddedResultDigit in zip(value2, paddedResult):
        if hadResultDigit:
            firstMultLine = "|/|"
        else:
            firstMultLine = "| |"
        secondMultLine = "| |"
        thirdMultLine = "|{}|".format(paddedResultDigit)
        hadResultDigit = paddedResultDigit != " "
        for digit1 in value1:
            product = "0{}".format(int(digit1) * int(digit2))
            firstMultLine += "{} /|".format(product[-2])
            secondMultLine += " / |"
            thirdMultLine += "/ {}|".format(product[-1])

        firstMultLine += " |"
        secondMultLine += "{}|".format(digit2)
        thirdMultLine += " |"

        print(firstMultLine)
        print(secondMultLine)
        print(thirdMultLine)
        print(thirdLine)


    resultLine = "|"
    for digit in result[-len(value1):]:
        if hadResultDigit:
            resultLine += "/ {} ".format(digit)
        else:
            resultLine += "  {} ".format(digit)
    resultLine += "   |"
    print(resultLine)
    print(firstLine)
