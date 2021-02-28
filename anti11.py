memoized = {}
def testMemoized(length, wasPreviousOne):
    key = (length, wasPreviousOne)
    if key not in memoized:
        memoized[key] = testRecursive(length, wasPreviousOne)

    return memoized[key]

def testRecursive(length, wasPreviousOne):
    if length == 0:
        return 1

    recursiveResult = 0
    recursiveResult += testMemoized(length - 1, False)
    if not wasPreviousOne:
        recursiveResult += testMemoized(length - 1, True)

    return recursiveResult

def testIterate(length):
    for currentLength in range(length):
        testMemoized(currentLength, False)
        testMemoized(currentLength, True)

    return testMemoized(length, False)


numberOfTests = int(input())
for _ in range(numberOfTests):
    requiredLength = int(input())
    result = testIterate(requiredLength) % (10 ** 9 + 7)
    print(result)
