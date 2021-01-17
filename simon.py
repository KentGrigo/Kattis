numberOfCommands = int(input())

for _ in range(numberOfCommands):
    line = input()
    if "simon says" in line:
        print(line[11:])
    else:
        print("")
