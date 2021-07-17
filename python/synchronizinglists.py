def test(lines1, lines2):
    sortedLines1 = sorted(lines1)
    sortedLines2 = sorted(lines2)
    orderedLines2 = [None] * numberOfLines
    for sortedLine1, sortedLine2 in zip(sortedLines1, sortedLines2):
        orderedIndex = lines1.index(sortedLine1)
        orderedLines2[orderedIndex] = sortedLine2

    for orderedLine2 in orderedLines2:
        print(orderedLine2)


isFirst = True
while True:
    numberOfLines = int(input())
    if numberOfLines == 0:
        break

    if not isFirst:
        print("")
    else:
        isFirst = False

    lines1 = []
    lines2 = []

    for _ in range(numberOfLines):
        line = int(input())
        lines1.append(line)

    for _ in range(numberOfLines):
        line = int(input())
        lines2.append(line)

    test(lines1, lines2)
