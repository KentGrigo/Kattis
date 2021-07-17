numberOfMinions = int(input())
minions = []
for _ in range(numberOfMinions):
    lowerBound, upperBound = list(map(int, input().split()))
    minions.append((lowerBound, upperBound))

minions.sort(key = lambda bounds: bounds[1])
numberOfRooms = 0
latestUpperBound = 0
for (lowerBound, upperBound) in minions:
    if latestUpperBound < lowerBound:
        numberOfRooms += 1
        latestUpperBound = upperBound

print(numberOfRooms)
