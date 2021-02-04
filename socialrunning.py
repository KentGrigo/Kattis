numberOfFriends = int(input())
distances = []
for _ in range(numberOfFriends):
    distance = int(input())
    distances.append(distance)

distances = 2 * distances
maxValue = 10 ** 4
minDistance = 2 * maxValue
for distance1, distance2 in zip(distances[:-2], distances[2:]):
    minDistance = min(minDistance, distance1 + distance2)

print(minDistance)
