from collections import Counter

numberOfTests = int(input())
for _ in range(numberOfTests):
    number = input()
    maximumNumberOfOnes = 0
    for index in range(1, len(number) + 1):
        subNumber = int(number[0:index])
        binary = "{0:b}".format(subNumber)
        numberOfOnes = Counter(binary)['1']
        maximumNumberOfOnes = max(maximumNumberOfOnes, numberOfOnes)

    print(maximumNumberOfOnes)
