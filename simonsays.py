numberOfCommands = int(input())

for _ in range(numberOfCommands):
    words = input().split()
    if words[0] == "Simon" and words[1] == "says":
        print(' '.join(words[2:]))
