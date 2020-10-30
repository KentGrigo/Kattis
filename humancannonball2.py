import math

numberOfTests = int(input())

for _ in range(numberOfTests):
    data = input().split()
    v0 = float(data[0])
    angle = float(data[1])
    x1 = float(data[2])
    height1 = float(data[3])
    height2 = float(data[4])
    gravity = 9.81

    radians = math.radians(angle)

    timeAtX1 = x1 / (v0 * math.cos(radians))

    flight = v0 * timeAtX1 * math.sin(radians)
    fall = 1/2 * gravity * (timeAtX1 ** 2)
    heightAtX1 = flight - fall

    if height1 + 1 <= heightAtX1 and heightAtX1 <= height2 - 1:
        print("Safe")
    else:
        print("Not Safe")
