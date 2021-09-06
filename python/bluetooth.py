numberOfProblems = int(input())

locationToNumberOfTeeth = {}
locationToNumberOfTeeth["left+"] = 8
locationToNumberOfTeeth["left-"] = 8
locationToNumberOfTeeth["right+"] = 8
locationToNumberOfTeeth["right-"] = 8

locationToNumberOfBlueTeeth = {}
locationToNumberOfBlueTeeth["left+"] = 0
locationToNumberOfBlueTeeth["left-"] = 0
locationToNumberOfBlueTeeth["right+"] = 0
locationToNumberOfBlueTeeth["right-"] = 0

for _ in range(numberOfProblems):
    position, condition = input().split()
    if position[0] == "+":
        location = "left+"
    elif position[0] == "-":
        location = "left-"
    elif position[1] == "+":
        location = "right+"
    else:
        location = "right-"

    if condition == "m":
        locationToNumberOfTeeth[location] -= 1
    else:
        locationToNumberOfBlueTeeth[location] -= 1

numberOfNeededTeeth = 1
if numberOfNeededTeeth <= locationToNumberOfTeeth["left+"] and \
    numberOfNeededTeeth <= locationToNumberOfTeeth["left-"] and \
    locationToNumberOfBlueTeeth["left+"] == 0 and \
    locationToNumberOfBlueTeeth["left-"] == 0:
        print("0")
elif numberOfNeededTeeth <= locationToNumberOfTeeth["right+"] and \
    numberOfNeededTeeth <= locationToNumberOfTeeth["right-"] and \
    locationToNumberOfBlueTeeth["right+"] == 0 and \
    locationToNumberOfBlueTeeth["right-"] == 0:
        print("1")
else:
    print("2")
