import math

def areaOfCircle(radius):
    return math.pi * radius ** 2

data = input().split()
pizzaRadius = int(data[0])
crustLength = int(data[1])

chessRadius = pizzaRadius - crustLength
chessArea = areaOfCircle(chessRadius)
pizzaArea = areaOfCircle(pizzaRadius)
chessRatio = chessArea / pizzaArea * 100
print(chessRatio)
