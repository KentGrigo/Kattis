def isMatchingWord(word, hexagonLetters):
    for letter in word:
        if letter not in hexagonLetters:
            return False

    return True


hexagonLetters = input()
mandatoryFirstHexagonletter = hexagonLetters[0]

numberOfDictionaryWords = int(input())
for _ in range(numberOfDictionaryWords):
    dictionaryWord = input()
    if len(dictionaryWord) < 4:
        continue

    if mandatoryFirstHexagonletter not in dictionaryWord:
        continue

    if isMatchingWord(dictionaryWord, hexagonLetters):
        print(dictionaryWord)
