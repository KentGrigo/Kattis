# Extended Euclidean algorithm
def inverse(a, n):
    t = 0; newT = 1
    r = n; newR = a

    while newR != 0:
        quotient = r // newR
        t, newT = (newT, t - quotient * newT) 
        r, newR = (newR, r - quotient * newR)

    if 1 < r:
        return -1
    if t < 0:
        t = t + n

    return t

def compute(value1, operator, value2):
    if operator == "+":
        result = value1 + value2
    elif operator == "-":
        result = value1 - value2
    elif operator == "*":
        result = value1 * value2
    else: # multiplication with modular inverse of `value2`
        inverseValue2 = inverse(value2, limit)
        if inverseValue2 == -1:
            return -1

        result = value1 * inverseValue2

    result %= limit
    return result


while True:
    limit, numberOfExpressions = list(map(int, input().split()))
    if limit == 0 and numberOfExpressions == 0:
        break

    for _ in range(numberOfExpressions):
        expression = input().split()
        value1 = int(expression[0])
        operator = expression[1]
        value2 = int(expression[2])
        result = compute(value1, operator, value2)
        print(result)
