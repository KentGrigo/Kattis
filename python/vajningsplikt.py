def isOpposite(exit1, exit2):
    horizontal = ["North", "South"]
    vertical = ["West", "East"]

    isDifferent = exit1 != exit2
    isVertical = exit1 in vertical and exit2 in vertical
    isHorizontal = exit1 in horizontal and exit2 in horizontal
    return isDifferent and (isVertical or isHorizontal)

def isRight(exit1, exit2):
    ordering = ["North", "East", "South", "West"]
    rightIndex = ordering.index(exit1) - 1
    return exit2 == ordering[rightIndex]

def isLeft(exit1, exit2):
    return isRight(exit2, exit1)


startCar1, endCar1, startCar2 = input().split()
type1 = isOpposite(startCar1, endCar1) and isRight(startCar1, startCar2)
type2 = isLeft(startCar1, endCar1) and (isOpposite(startCar1, startCar2) or isRight(startCar1, startCar2))
mustYield = type1 or type2
if mustYield:
    print("Yes")
else:
    print("No")
