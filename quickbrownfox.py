def getAllLetters():
    allLetters = []
    aAscii = ord("a")
    zAscii = ord("z")
    for letterAscii in range(aAscii, zAscii + 1):
        letter = chr(letterAscii)
        allLetters.append(letter)

    return allLetters

def computeIsPangram(phrase):
    allLetters = getAllLetters()
    for letter in phrase:
        lowercaseLetter = letter.lower()
        try:
            allLetters.remove(lowercaseLetter)
        except ValueError:
            pass

    if allLetters:
        print("missing {}".format("".join(allLetters)))
    else:
        print("pangram")


numberOfPhrases = int(input())
for _ in range(numberOfPhrases):
    phrase = list(input())
    computeIsPangram(phrase)
