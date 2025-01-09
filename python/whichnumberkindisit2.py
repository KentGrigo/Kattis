import math

numberOfTests = int(input())
for _ in range(numberOfTests):
    value = int(input())
    isOdd = value % 2 == 1
    isSquare = value == int(math.sqrt(value)) ** 2
    if isOdd and isSquare:
        print("OS")
    elif isOdd:
        print("O")
    elif isSquare:
        print("S")
    else:
        print("EMPTY")
