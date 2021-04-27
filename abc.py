a, b, c = sorted(list(map(int, input().split())))
order = list(input())

output = ""
for element in order:
    if output != "":
        output += " "

    if element == "A":
        output += str(a)
    elif element == "B":
        output += str(b)
    else: # if element == "C":
        output += str(c)

print(output)
