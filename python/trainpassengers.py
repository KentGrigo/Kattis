capacity, numberOfStations = list(map(int, input().split()))
isPossible = True
numberOfPassengers = 0
for _ in range(numberOfStations):
    numberLeaving, numberEntering, numberStaying = list(map(int, input().split()))

    numberOfPassengers -= numberLeaving
    if numberOfPassengers < 0:
        isPossible = False

    numberOfPassengers += numberEntering
    if capacity < numberOfPassengers:
        isPossible = False

    if numberOfPassengers < capacity and 0 < numberStaying:
        isPossible = False

if numberOfPassengers != 0:
    isPossible = False

if isPossible:
    print("possible")
else:
    print("impossible")
