while True:
    numberOfLettersToSkip = int(input())
    if numberOfLettersToSkip == 0:
        break

    plainText = input()
    intermediateText = list(plainText.replace(" ", "").upper())
    cipherText = [" "] * len(intermediateText)
    startIndex = 0
    index = 0
    for letter in intermediateText:
        cipherText[index] = letter
        index += numberOfLettersToSkip
        if len(intermediateText) <= index:
            startIndex += 1
            if numberOfLettersToSkip <= startIndex:
                break

            index = startIndex

    cipherText = "".join(cipherText)
    print(cipherText)
