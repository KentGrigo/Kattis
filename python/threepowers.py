def isEven(value):
    return value % 2 == 0


multiplier = 3
while True:
    index = int(input())
    if index == 0:
        break

    index -= 1
    subset = []
    currentValue = 1
    while index:
        if not isEven(index):
            subset.append(str(currentValue))

        currentValue *= multiplier
        index = index >> 1

    if subset:
        print("{{ {} }}".format(", ".join(subset)))
    else:
        print("{ }")
