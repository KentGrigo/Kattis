from collections import Counter

def isMultigram(word, wordLength, anagramLength):
    anagram = Counter(word[:anagramLength])
    for index in range(anagramLength, wordLength, anagramLength):
        potentialMultigram = Counter(word[index : index + anagramLength])
        if anagram != potentialMultigram:
            return False

    return True

def computeMultigramLength(word):
    wordLength = len(word)
    for anagramLength in range(1, wordLength // 2 + 1):
        if wordLength % anagramLength != 0:
            continue

        if isMultigram(word, wordLength, anagramLength):
            return anagramLength

    return None


word = input()
anagramLength = computeMultigramLength(word)
if anagramLength is None:
    print(-1)
else:
    anagram = word[:anagramLength]
    print("".join(anagram))
