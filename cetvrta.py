point1 = input().split()
point2 = input().split()
point3 = input().split()

x1 = int(point1[0])
y1 = int(point1[1])

x2 = int(point2[0])
y2 = int(point2[1])

x3 = int(point3[0])
y3 = int(point3[1])

def missingCoordinate(coordinate1, coordinate2, coordinate3):
    if (coordinate1 == coordinate2):
        return coordinate3
    elif (coordinate1 == coordinate3):
        return coordinate2
    else:
        return coordinate1

missingX = missingCoordinate(x1, x2, x3)
missingY = missingCoordinate(y1, y2, y3)

print("{} {}".format(missingX, missingY))