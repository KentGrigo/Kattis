numberOfNumbers, numberOfCheats = list(map(int, input().split()))
numberToCount = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
for _ in range(numberOfNumbers):
    number = int(input())
    numberToCount[number] += 1

mostOccurringNumber = max(numberToCount, key = numberToCount.get)
mostOccurrences = numberToCount[mostOccurringNumber]
requiredNumberOfCheats = numberOfNumbers - mostOccurrences
canWinWithCheat = requiredNumberOfCheats <= numberOfCheats
if canWinWithCheat:
    print('Ja')
else:
    print('Nej')
