memoized = {}

def interleavingsMemoized(numberOfValues1, numberOfValues2):
    key = (numberOfValues1, numberOfValues2)
    if key not in memoized:
        memoized[key] = interleavings(numberOfValues1, numberOfValues2)

    return memoized[key]

def interleavings(numberOfValues1, numberOfValues2):
    if numberOfValues1 == 0 or numberOfValues2 == 0:
        return 1
    else:
        return interleavingsMemoized(numberOfValues1 - 1, numberOfValues2) + interleavingsMemoized(numberOfValues1, numberOfValues2 - 1)

def test(values):
    numberOfValues = len(values)
    if numberOfValues == 0 or numberOfValues == 1:
        return 1

    pivot = values[0]
    restValues = values[1:]
    smallerRestValues = list(filter(lambda restValue: restValue < pivot, restValues))
    biggerOrEqualRestValues = list(filter(lambda restValue: pivot <= restValue, restValues))
    numberOfInterleavings = interleavingsMemoized(len(smallerRestValues), len(biggerOrEqualRestValues))

    recursive1 = test(smallerRestValues)
    recursive2 = test(biggerOrEqualRestValues)

    return numberOfInterleavings * recursive1 * recursive2


while True:
    numberOfValues = int(input())
    if numberOfValues == 0:
        break

    values = list(map(int, input().split()))
    print(test(values))
