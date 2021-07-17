def evaluate(value1, operator, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 // value2

def test(operators, a, b, c, d):
    equations = 0
    for operator1 in operators:
        for operator2 in operators:
            if operator1 == "/" and b == 0 or \
                operator2 == "/" and d == 0:
                    continue

            resultLeft = evaluate(a, operator1, b)
            resultRight = evaluate(c, operator2, d)
            if resultLeft == resultRight:
                equations += 1
                print("{} {} {} = {} {} {}".format(a, operator1, b, c, operator2, d))

    if equations == 0:
        print("problems ahead")


operators = ["*", "+", "-", "/"]
a, b, c, d = list(map(int, input().split()))
test(operators, a, b, c, d)
