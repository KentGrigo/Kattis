numberOfCars, decelerationConstant = list(map(int, input().split()))
distances = list(map(int, input().split()))
distances.sort()

distanceToNearestCar = distances[0]
maxSafeDistanceToNearestCar = 0
for carsInbetween, distance in enumerate(distances):
    safeDistanceToCurrentCar = decelerationConstant * (carsInbetween + 1)
    safeDistanceToNearestCar = safeDistanceToCurrentCar - (distance - distanceToNearestCar)
    maxSafeDistanceToNearestCar = max(maxSafeDistanceToNearestCar, safeDistanceToNearestCar)

print(maxSafeDistanceToNearestCar)
