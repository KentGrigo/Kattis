numberOfTests = int(input())
for _ in range(numberOfTests):
    testNumber, base, number = list(map(int, input().split()))
    result = 0
    while 0 < number:
        cipher = number % base
        number //= base
        result += cipher ** 2

    print("{} {}".format(testNumber, result))
