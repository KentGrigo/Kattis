quadkey = input()
level = len(quadkey)
x = 0
y = 0
for cipher in quadkey:
    x *= 2
    y *= 2

    cipher = int(cipher)
    if cipher == 1 or cipher == 3:
        x += 1

    if cipher == 2 or cipher == 3:
        y += 1

print("{} {} {}".format(level, x, y))
