numberOfRods = int(input())
totalLength = 0
for _ in range(numberOfRods):
    rodLength = int(input())
    if totalLength == 0:
        totalLength += 1

    totalLength += rodLength - 1

print(totalLength)
