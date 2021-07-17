numberOfSamples = int(input())

previousTime = None
previousValue = None
totalArea = 0
for _ in range(numberOfSamples):
    data = input().split()
    time = int(data[0])
    value = float(data[1])

    if previousTime is not None and previousValue is not None:
        area = (previousValue + value) / 2 * (time - previousTime)
        totalArea += area

    previousTime = time
    previousValue = value

print(totalArea / 1000)
