data = input().split()
numberOfLevelJunctions = int(data[0])
numberOfSwitches = int(data[1])

hasEvenNumberOfSwitches = numberOfSwitches % 2 == 0
if hasEvenNumberOfSwitches:
    print("possible")
else:
    print("impossible")