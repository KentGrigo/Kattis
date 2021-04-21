numberOfLists, numberOfItems = list(map(int, input().split()))
isFirstList = True
recurringElements = set()
for _ in range(numberOfLists):
    shoppingElements = set(input().split())
    if isFirstList:
        isFirstList = False
        recurringElements.update(shoppingElements)
    else:
        recurringElements = recurringElements.intersection(shoppingElements)

sortedElements = sorted(recurringElements)
print(len(sortedElements))
for element in sortedElements:
    print(element)
