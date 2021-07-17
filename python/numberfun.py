import operator

numberOfTests = int(input())

def check(value1, value2, result, operation):
    return operation(value1, value2) == result

def checkOperations(value1, value2, result):
    return check(value1, value2, result, operator.add) \
        or check(value1, value2, result, operator.sub) \
        or check(value1, value2, result, operator.mul) \
        or check(value1, value2, result, operator.truediv)

for _ in range(numberOfTests):
    data = input().split()
    value1 = int(data[0])
    value2 = int(data[1])
    result = int(data[2])

    canProduceResult = checkOperations(value1, value2, result) or checkOperations(value2, value1, result)
    if canProduceResult:
        print("Possible")
    else:
        print("Impossible")
