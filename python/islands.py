def computeNumberOfIslands(elements):
    numberOfIslands = 0
    stack = [0]
    for currentElement in elements:
        previousElement = stack[-1]
        if previousElement < currentElement:
            numberOfIslands += 1
            stack.append(currentElement)
        elif previousElement == currentElement:
            pass
        else: # currentElement < previousElement
            while currentElement < stack[-1]:
                stack.pop()

            if stack[-1] < currentElement:
                numberOfIslands += 1
                stack.append(currentElement)

    return numberOfIslands


numberOfTests = int(input())
for _ in range(numberOfTests):
    testNumber, *elements = list(map(int, input().split()))
    numberOfIslands = computeNumberOfIslands(elements)
    print(testNumber, numberOfIslands)
