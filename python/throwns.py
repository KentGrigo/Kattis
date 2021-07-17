numberOfStudents, numberOfCommands = list(map(int, input().split()))
commands = input().split()
positions = [0]
index = 0
while index < len(commands):
    command = commands[index]
    if command == "undo":
        numberOfUndos = int(commands[index + 1])
        for _ in range(numberOfUndos):
            positions.pop()

        index += 2
    else:
        currentPosition = positions[-1]
        nextPosition = (currentPosition + int(command)) % numberOfStudents
        positions.append(nextPosition)
        index += 1

print(positions[-1])
