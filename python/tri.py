def findOperator(number1, number2, result):
    operators = ["+", "-", "*", "/"]
    combinations = [number1 + number2, number1 - number2, number1 * number2, number1 / number2]
    if result in combinations:
        indexOfResult = combinations.index(result)
        return operators[indexOfResult]

    return None


number1, number2, number3 = list(map(int, input().split()))
operator1 = findOperator(number1, number2, number3)
operator2 = findOperator(number2, number3, number1)
if operator1 is not None:
    print("{}{}{}={}".format(number1, operator1, number2, number3))
else:
    print("{}={}{}{}".format(number1, number2, operator2, number3))
