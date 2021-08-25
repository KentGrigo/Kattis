def findLetterLocation(keyboardLayout, letter):
    for rowNumber, row in enumerate(keyboardLayout):
        for columnNumber, key in enumerate(row):
            if letter == key:
                return (rowNumber, columnNumber)

    return None

def findWordLocations(keyboardLayout, word):
    letterLocations = []
    for letter in word:
        letterLocation = findLetterLocation(keyboardLayout, letter)
        letterLocations.append(letterLocation)

    return letterLocations


keyboardLayout = [
    list("qwertyuiop"),
    list("asdfghjkl"),
    list("zxcvbnm"),
]
numberOfTests = int(input())
for _ in range(numberOfTests):
    typedWord, dictionarySize = input().split()
    typedLetterLocations = findWordLocations(keyboardLayout, typedWord)

    numberOfSpellCheckEntries = int(dictionarySize)
    distanceAndWords = []
    for _ in range(numberOfSpellCheckEntries):
        word = input()
        letterLocations = findWordLocations(keyboardLayout, word)

        distance = 0
        for (typedRowNumber, typedColumnNumber), (rowNumber, columnNumber) in zip(typedLetterLocations, letterLocations):
            letterDistance = abs(typedRowNumber - rowNumber) + abs(typedColumnNumber - columnNumber)
            distance += letterDistance

        distanceAndWords.append((distance, word))

    distanceAndWords.sort()
    for distance, word in distanceAndWords:
        print(word, distance)
