numberOfTests = int(input())
for _ in range(numberOfTests):
    data = input().split()
    numberOfRotationsAndCuts = int(data[0])
    sentence = data[1]

    isUpsideDown = False
    startIndex = 0
    endIndex = len(sentence)
    for _ in range(numberOfRotationsAndCuts):
        length = endIndex - startIndex
        quarterLength = length // 4
        if quarterLength == 0:
            break

        if not isUpsideDown:
            startIndex += quarterLength
        else:
            endIndex -= quarterLength

        isUpsideDown = not isUpsideDown

    resultingText = sentence[startIndex:endIndex]
    print(resultingText)
