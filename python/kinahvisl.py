initialWord = input()
endWord = input()
numberOfChanges = 0
for initialLetter, endLetter in zip(initialWord, endWord):
    if initialLetter != endLetter:
        numberOfChanges += 1

minimumNumberOfChildren = numberOfChanges + 1
print(minimumNumberOfChildren)
