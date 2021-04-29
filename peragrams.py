from collections import Counter

text = list(input())
counter = Counter(text)
numberOfOddOccurrences = 0
for occurrences in counter.values():
    isOdd = occurrences % 2 == 1
    if isOdd:
        numberOfOddOccurrences += 1

if numberOfOddOccurrences == 0 or numberOfOddOccurrences == 1:
    numberOfLettersToRemove = 0
else:
    numberOfLettersToRemove = numberOfOddOccurrences - 1

print(numberOfLettersToRemove)
