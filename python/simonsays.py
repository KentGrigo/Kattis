numberOfCommands = int(input())

for _ in range(numberOfCommands):
    line = input()
    if "Simon says" in line:
        print(line[11:])
