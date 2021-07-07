numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfStops = int(input())
    numberOfPassengers = 0
    for _ in range(numberOfStops):
        numberOfPassengers += 0.5
        numberOfPassengers *= 2

    print(int(numberOfPassengers))
