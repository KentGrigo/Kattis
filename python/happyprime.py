def generatePrimes(limit):
    primeMask = [True] * limit
    primeMask[0] = False
    primeMask[1] = False
    primes = []
    for number in range(limit):
        if not primeMask[number]:
            continue

        primes.append(number)
        for notPrime in range(number * number, limit, number):
            primeMask[notPrime] = False

    return primes

def isHappy(number, happyMask):
    def computeSquaredSum(number):
        sum = 0
        for cipher in str(number):
            cipher = int(cipher)
            sum += cipher ** 2

        return sum

    def helper(number):
        if number in happyMask:
            return happyMask[number]

        if number in visited:
            return False

        visited.add(number)
        squaredSum = computeSquaredSum(number)
        result = helper(squaredSum)
        happyMask[number] = result
        return result

    visited = set()
    return helper(number)

def generateHappyNumbers(limit):
    happyMask = {}
    happyMask[0] = False
    happyMask[1] = True
    for number in range(limit):
        if number in happyMask:
            continue

        isHappy(number, happyMask)

    happyNumbers = []
    for number in range(limit):
        if happyMask[number]:
            happyNumbers.append(number)

    return happyNumbers


limit = 10001
primes = generatePrimes(limit)
happyNumbers = generateHappyNumbers(limit)
numberOfTests = int(input())
for _ in range(numberOfTests):
    testNumber, number = list(map(int, input().split()))
    if number in primes and number in happyNumbers:
        result = "YES"
    else:
        result = "NO"

    print("{} {} {}".format(testNumber, number, result))
