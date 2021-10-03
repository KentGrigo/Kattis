from collections import Counter

height, width = list(map(int, input().split()))
mask = [False] * width
for _ in range(height):
    line = input()
    for index, letter in enumerate(line):
        if letter == "$":
            mask[index] = True

count = Counter(mask)
numberOfMoves = count[False] + 1
print(numberOfMoves)
