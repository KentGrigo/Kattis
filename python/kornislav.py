distances = list(map(lambda distance: int(distance), input().split()))
distances.sort()
maxArea = distances[0] * distances[2]
print(maxArea)
