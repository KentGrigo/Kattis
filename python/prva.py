def rotate(crossword):
    return zip(*crossword)

numberOfRows, numberOfColumns = list(map(int, input().split()))
rows = []
for _ in range(numberOfRows):
    row = list(input())
    rows.append(row)

allWords = []
for row in rows:
    words = "".join(row).split("#")
    for word in words:
        if 2 <= len(word):
            allWords.append(word)

rows = rotate(rows)
for row in rows:
    words = "".join(row).split("#")
    for word in words:
        if 2 <= len(word):
            allWords.append(word)

allWords.sort()
print(allWords[0])
