numberOfTests = int(input())
for testNumber in range(1, numberOfTests + 1):
    numberOfSegments = int(input())
    segments = input().split()
    redSegments = []
    blueSegments = []
    for segment in segments:
        color = segment[-1]
        length = int(segment[:-1])
        if color == "R":
            redSegments.append(length)
        else:
            blueSegments.append(length)

    redSegments.sort(reverse = True)
    blueSegments.sort(reverse = True)
    totalLength = 0
    for redSegment, blueSegment in zip(redSegments, blueSegments):
        totalLength += redSegment + blueSegment - 2

    print("Case #{}: {}".format(testNumber, totalLength))
