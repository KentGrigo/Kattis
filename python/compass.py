currentPosition = int(input())
nextPosition = int(input())

difference = nextPosition - currentPosition
if -180 < difference <= 180:
    print(difference)
elif -180 < difference + 360 <= 180:
    print(difference + 360)
elif -180 < difference - 360 <= 180:
    print(difference - 360)
