program = input()

nopCount = 0
for index, token in enumerate(program):
    if token.isupper():
        extraNops = (4 - (index + nopCount) % 4) % 4
        nopCount += extraNops

print(nopCount)
