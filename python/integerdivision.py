memoization = {}
def divide(numerator, divisor):
    if numerator not in memoization:
        result = numerator // divisor
        memoization[numerator] = result

    return memoization[numerator]


numberOfNumerators, divisor = list(map(int, input().split()))
numerators = list(map(int, input().split()))
numerators.sort()

numberOfPairs = 0
matchStreak = 0
for prevNumerator, nextNumerator in zip(numerators[:-1], numerators[1:]):
    if nextNumerator == prevNumerator or \
        (nextNumerator - prevNumerator <= divisor and \
        divide(prevNumerator, divisor) == divide(nextNumerator, divisor)):
            matchStreak += 1
    else:
        matchStreak = 0

    numberOfPairs += matchStreak

print(numberOfPairs)
