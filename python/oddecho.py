numberOfWords = int(input())
isOdd = False
for _ in range(numberOfWords):
    isOdd = not isOdd
    word = input()
    if isOdd:
        print(word)
