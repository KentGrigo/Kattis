def findIntersection(wordA, wordB):
    for indexA, letterA in enumerate(wordA):
        for indexB, letterB in enumerate(wordB):
            if letterA == letterB:
                return (indexA, indexB)

    return None


wordA, wordB = input().split()
intersection = findIntersection(wordA, wordB)
crossword = []
for letterB in wordB:
    entry = list("." * len(wordA))
    entry[intersection[0]] = letterB
    crossword.append(entry)

for indexA, letterA in enumerate(wordA):
    crossword[intersection[1]][indexA] = letterA

for entry in crossword:
    print("".join(entry))
