words = input().split()
seenWords = []


for word in words:
    for seenWord in seenWords:
        if word == seenWord:
            print("no")
            exit()
    seenWords.append(word)

print("yes")