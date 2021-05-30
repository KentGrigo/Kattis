numberOfCars, lengthOfCar, numberOfPassengers = list(map(int, input().split()))
carToNumberOfPeople = {}
maxDistance = 0
for _ in range(numberOfPassengers):
    location = int(input())
    closestCar = location // lengthOfCar
    closestCar = min(closestCar, numberOfCars - 1)
    carToNumberOfPeople[closestCar] = 1 + carToNumberOfPeople.get(closestCar, 0)
    distance = abs((closestCar * lengthOfCar + lengthOfCar // 2) - location)
    maxDistance = max(distance, maxDistance)

print(maxDistance)
print(max(carToNumberOfPeople.values()))
