words = []
while True:
    try:
        newWords = input().split()
    except EOFError:
        break

    words.extend(newWords)

compoundWords = set()
for index, word1 in enumerate(words):
    for word2 in words[index + 1:]:
        compoundWords.add(word1 + word2)
        compoundWords.add(word2 + word1)

compoundWords = sorted(compoundWords)
for compoundWord in compoundWords:
    print(compoundWord)
