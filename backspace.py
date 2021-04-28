line = list(input())
output = []
for character in line:
    if character == "<":
        output.pop()
    else:
        output.append(character)

print("".join(output))
