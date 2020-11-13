import math

data = input().split()
height = int(data[0])
angle = int(data[1])

radiants = math.radians(angle)
ladderLength = math.ceil(height / math.sin(radiants))
print(ladderLength)
