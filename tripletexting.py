line = input()
lengthOfLine = len(line) // 3
words = [line[0:lengthOfLine], line[lengthOfLine:2 * lengthOfLine], line[2 * lengthOfLine:]]
if words[0] == words[1] or words[0] == words[2]:
    print(words[0])
else:
    print(words[1])
