from collections import Counter

def solveProblemType1(numbers):
    def helper():
        table = {number: True for number in numbers}
        for x in numbers:
            y = 7777 - x
            if x == y:
                continue

            if y in table:
                return True

        return False

    hasSolution = helper()
    if hasSolution:
        print("Yes")
    else:
        print("No")

def solveProblemType2(numbers):
    hasDuplicates = len(numbers) != len(set(numbers))
    if hasDuplicates:
        print("Contains duplicate")
    else:
        print("Unique")

def solveProblemType3(numbers):
    def helper():
        numberToCount = Counter(numbers)
        half = numberOfNumbers / 2
        for number, count in numberToCount.items():
            if half < count:
                return number

        return None

    majorityElement = helper()
    if majorityElement is None:
        print("-1")
    else:
        print(majorityElement)

def solveProblemType4(numbers):
    numbers.sort()
    hasEvenNumberOfNumbers = numberOfNumbers & 1 == 0
    if hasEvenNumberOfNumbers:
        print(numbers[numberOfNumbers // 2 - 1], numbers[numberOfNumbers // 2])
    else:
        print(numbers[numberOfNumbers // 2])

def solveProblemType5(numbers):
    sortedLeftovers = map(str, sorted(filter(lambda number: 100 <= number <= 999, numbers)))
    print(" ".join(sortedLeftovers))


numberOfNumbers, problemType = list(map(int, input().split()))
numbers = list(map(int, input().split()))
if problemType == 1:
    solveProblemType1(numbers)
elif problemType == 2:
    solveProblemType2(numbers)
elif problemType == 3:
    solveProblemType3(numbers)
elif problemType == 4:
    solveProblemType4(numbers)
elif problemType == 5:
    solveProblemType5(numbers)
