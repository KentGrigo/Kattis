def clamp(value, smallest, largest):
    return max(smallest, min(value, largest))

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def changePosition(self, direction, numberOfSteps):
        return {
            "u": lambda: self._changePosition(0, numberOfSteps),
            "d": lambda: self._changePosition(0, -numberOfSteps),
            "l": lambda: self._changePosition(-numberOfSteps, 0),
            "r": lambda: self._changePosition(numberOfSteps, 0),
        }[direction]()

    def _changePosition(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY
        return self

    def adaptBounds(self, width, length):
        self.x = clamp(self.x, 0, width)
        self.y = clamp(self.y, 0, length)

    def __repr__(self):
        return "{} {}".format(self.x, self.y)


while True:
    width, length = list(map(int, input().split()))
    if width == 0 and length == 0:
        break

    actualPosition = Position(0, 0)
    expectedPosition = Position(0, 0)
    numberOfSegments = int(input())
    for _ in range(numberOfSegments):
        direction, numberOfSteps = input().split()
        numberOfSteps = int(numberOfSteps)
        actualPosition.changePosition(direction, numberOfSteps)\
                      .adaptBounds(width - 1, length - 1)
        expectedPosition.changePosition(direction, numberOfSteps)

    print("Robot thinks", expectedPosition)
    print("Actually at", actualPosition)
    print("")
