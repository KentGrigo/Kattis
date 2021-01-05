seenWords = []
while True:
    try:
        words = input().split()
    except EOFError:
        break

    optimizedWords = []
    for word in words:
        if word.lower() in seenWords:
            optimizedWords.append(".")
        else:
            optimizedWords.append(word)
            seenWords.append(word.lower())
    
    print(" ".join(optimizedWords))
