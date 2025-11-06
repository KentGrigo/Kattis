print('Gnomes:')
numberOfLines = int(input())
for lineNumber in range(numberOfLines):
    length1, length2, length3 = list(map(int, input().split()))
    isIncreasingOrder = length1 < length2 < length3
    isDecreasingOrder = length3 < length2 < length1
    if isIncreasingOrder or isDecreasingOrder:
        print('Ordered')
    else:
        print('Unordered')
