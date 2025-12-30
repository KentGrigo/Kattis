numberOfStops = int(input())

currentNumberOfPassengers = 0
peakNumberOfPassengers = 0
for stopNumber in range(numberOfStops):
    numberOfPassengersGettingOff, numberOfPassengersGettingOn = list(map(int, input().split()))
    currentNumberOfPassengers -= numberOfPassengersGettingOff
    currentNumberOfPassengers += numberOfPassengersGettingOn
    peakNumberOfPassengers = max(peakNumberOfPassengers, currentNumberOfPassengers)

print(peakNumberOfPassengers)
