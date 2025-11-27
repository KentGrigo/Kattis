import math

tableDiameter = float(input())
spacePerKnight = float(input())
numberOfKnights = int(input())
totalSpaceForKnights = spacePerKnight * numberOfKnights
tableCircumference = tableDiameter * math.pi

if totalSpaceForKnights <= tableCircumference:
    print("YES")
else:
    print("NO")
