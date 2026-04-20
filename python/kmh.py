import math

def getDefaulSpeedLimit(previousHighestLimit):
    return math.ceil((previousHighestLimit + 1) / 10) * 10


numberOfSigns = int(input())
previousHighestLimit = 0
for _ in range(numberOfSigns):
    sign = input()
    if sign == '/':
        defaultSpeeLimit = getDefaulSpeedLimit(previousHighestLimit)
        print(defaultSpeeLimit)
    else:
        sign = int(sign)
        previousHighestLimit = max(sign, previousHighestLimit)
        print(sign)
