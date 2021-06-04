import base64

def isUnaryValue(operand):
    ciphers = set(operand)
    return len(ciphers) == 1 and "1" in ciphers

def convertUnary(operand1, operand2, operand3):
    if not (isUnaryValue(operand1) and isUnaryValue(operand2) and isUnaryValue(operand3)):
        return None

    return (len(operand1), len(operand2), len(operand3))

def convert(base, operand1, operand2, operand3):
    if base == 1:
        return convertUnary(operand1, operand2, operand3)

    try:
        return (int(operand1, base), int(operand2, base), int(operand3, base))
    except ValueError:
        return None

def evaluate(base, operator, operand1, operand2, operand3):
    values = convert(base, operand1, operand2, operand3)
    if values is None:
        return False

    (value1, value2, value3) = values
    result = {
        "+": value1 + value2,
        "*": value1 * value2,
        "-": value1 - value2,
        "/": value1 / value2,
    }[operator]
    return result == value3


bases = "@123456789abcdefghijklmnopqrstuvwxyz0"
minBase = 1
maxBase = 36
numberOfEquations = int(input())
for _ in range(numberOfEquations):
    operand1, operator, operand2, _, operand3 = input().split()
    validBases = ""
    for base in range(minBase, maxBase + 1):
        isValid = evaluate(base, operator, operand1, operand2, operand3)
        if isValid:
            encodedBase = bases[base]
            validBases += encodedBase

    if validBases == "":
        print("invalid")
    else:
        print(validBases)
