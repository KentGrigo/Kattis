order = list(map(int, input().split()))
isOrdered = False
while not isOrdered:
    isOrdered = True
    for index in range(len(order) - 1):
        prevElement = order[index]
        currElement = order[index + 1]
        if currElement < prevElement:
            isOrdered = False
            order[index] = currElement
            order[index + 1] = prevElement
            print(" ".join(str(element) for element in order))
