import re

words = input().split()
hardConsonants = "bcdgknptBCDGKNPT"
endings = ["ah", "oh", "uh"]

newWords = []
for word in words:
    firstCharacter = word[0]
    minDistance = 50
    bestHardConsonant = hardConsonants[0]
    for hardConsonant in hardConsonants:
        distance = abs(ord(hardConsonant) - ord(firstCharacter))
        if distance < minDistance:
            minDistance = distance
            bestHardConsonant = hardConsonant
    word = bestHardConsonant + word[1:]
    
    syllables = word.split("-")
    newWord = syllables[0]
    for syllable in syllables[1:]:
        newSyllable = re.sub("[{}]".format(hardConsonants), bestHardConsonant.lower(), syllable)
        newWord += newSyllable

    lastCharacter = newWord[-1]
    bestEnding = ""
    if lastCharacter in hardConsonants:
        minDistance = 50
        for ending in endings:
            distance = abs(ord(lastCharacter.lower()) - ord(ending[0]))
            if distance < minDistance:
                minDistance = distance
                bestEnding = ending

    newWord = bestHardConsonant + newWord[1:] + bestEnding
    newWords.append(newWord)

print(" ".join(newWords))
