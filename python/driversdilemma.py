tankCapacity, fuelLeak, distance = list(map(float, input().split()))
amountOfFuel = tankCapacity / 2
numberOfRows = 6
maxSpeed = None
for _ in range(numberOfRows):
    data = input().split()
    speed = int(data[0])
    fuelEfficiency = float(data[1])

    timeLeft = distance / speed
    fuelCost = distance / fuelEfficiency
    fuelLoss = timeLeft * fuelLeak
    hasEnoughFuel = fuelCost + fuelLoss <= amountOfFuel
    if hasEnoughFuel:
        maxSpeed = speed

if maxSpeed is None:
    print("NO")
else:
    print("YES {}".format(maxSpeed))
