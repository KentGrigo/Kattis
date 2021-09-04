modulo = 1000000007
numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfDigits = int(input())
    numberOfNumbersWithout9s = 8 * pow(9, numberOfDigits - 1, modulo)
    print(numberOfNumbersWithout9s % modulo)
