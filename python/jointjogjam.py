import math

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        diffX = self.x - other.x
        diffY = self.y - other.y
        return math.sqrt(diffX ** 2 + diffY ** 2)


positions = list(map(int, input().split()))
kariStart = Position(positions[0], positions[1])
olaStart = Position(positions[2], positions[3])
kariEnd = Position(positions[4], positions[5])
olaEnd = Position(positions[6], positions[7])

startDistance = kariStart.distance(olaStart)
endDistance = kariEnd.distance(olaEnd)
maxDistance = max(startDistance, endDistance)
print(maxDistance)
