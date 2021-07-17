def isVowel(character):
    return character in "aeiouy"

while True:
    try:
        words = input().split()
    except EOFError:
        break

    translatedWords = []
    for word in words:
        suffix = ""
        for character in word:
            if isVowel(character):
                break
            else:
                suffix += character
        
        if suffix == "":
            translatedWord = word + "yay"
        else:
            translatedWord = word[len(suffix):] + suffix + "ay"
        translatedWords.append(translatedWord)

    print(" ".join(translatedWords))
