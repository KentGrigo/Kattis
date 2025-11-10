height, width = list(map(int, input().split()))
letters = ['.'] * width
for _ in range(height):
    line = input()
    for columnNumber in range(width):
        letter = line[columnNumber]
        if letter != '.':
            letters[columnNumber] = letter

word = ''.join(letters)
print(word)
