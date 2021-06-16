def printDyslectionary(words):
    dyslectionary = [reversedWord[::-1] for reversedWord in sorted([word[::-1] for word in words])]
    lengthOfLongestWord = len(max(dyslectionary, key = len))
    for word in dyslectionary:
        print(word.rjust(lengthOfLongestWord))


words = []
while True:
    try:
        word = input()
        if word == "":
            printDyslectionary(words)
            words = []
            print("")
        else:
            words.append(word)

    except EOFError:
        break

printDyslectionary(words)
words = []
