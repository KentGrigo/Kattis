def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

numberOfCases = int(input())
for _ in range(numberOfCases):
    n = int(input())
    factorialDigit = factorial(n) % 10
    print(factorialDigit)

