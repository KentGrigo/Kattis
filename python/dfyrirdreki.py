a = int(input())
b = int(input())
c = int(input())

discriminant = b ** 2 - 4 * a * c
if 0 < discriminant:
    numberOfRoots = 2
elif discriminant == 0:
    numberOfRoots = 1
else:
    numberOfRoots = 0

print(numberOfRoots)
