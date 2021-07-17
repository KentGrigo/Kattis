data = input().split()
bTemperatureAtAZero = int(data[0])
bTemperatureIncrementPerOneOfA = int(data[1])

if bTemperatureIncrementPerOneOfA == 1:
    if bTemperatureAtAZero == 0:
        print("ALL GOOD")
    else:
        print("IMPOSSIBLE")
else:
    bIncrementSpeed = bTemperatureIncrementPerOneOfA - 1
    meetingPoint = -bTemperatureAtAZero / bIncrementSpeed
    print(meetingPoint)
