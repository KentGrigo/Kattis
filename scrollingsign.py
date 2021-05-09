def prevWordOverlapsCurrWord(prevWord, currWord):
    for prevWordStartIndex in range(wordLength):
        doesSuffixMatchPrefix = suffixMatchesPrefix(prevWordStartIndex, prevWord, currWord)
        if doesSuffixMatchPrefix:
            return prevWordStartIndex

    return wordLength

def suffixMatchesPrefix(prevWordStartIndex, prevWord, currWord):
    currWordIndex = 0
    for prevWordIndex in range(prevWordStartIndex, wordLength):
        prevWordLetter = prevWord[prevWordIndex]
        currWordLetter = currWord[currWordIndex]
        if prevWordLetter != currWordLetter:
            return False

        currWordIndex += 1

    return True


numberOfTests = int(input())
for _ in range(numberOfTests):
    wordLength, numberOfWords = list(map(int, input().split()))
    prevWord = list(input())
    numberOfLetters = wordLength
    for _ in range(numberOfWords - 1):
        currWord = list(input())
        overlapDegree = prevWordOverlapsCurrWord(prevWord, currWord)
        numberOfLetters += overlapDegree
        prevWord = currWord

    print(numberOfLetters)
