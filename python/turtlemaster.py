class Turtle:
    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY
        self.orientationIndex = 0
        self.orientation = ["right", "down", "left", "up"]

    def rotateClockwise(self):
        self.orientationIndex = (self.orientationIndex + 1) % len(self.orientation)

    def rotateCounterClockwise(self):
        self.orientationIndex = (self.orientationIndex - 1) % len(self.orientation)

    def fieldInFrontOf(self):
        currentOrientation = self.orientation[self.orientationIndex]
        return {
            "right": (self.x + 1, self.y),
            "left": (self.x - 1, self.y),
            "up": (self.x, self.y - 1),
            "down": (self.x, self.y + 1),
        }[currentOrientation]

    def move(self):
        (self.x, self.y) = self.fieldInFrontOf()

    def shoot(self, lines):
        (self.xForward, self.yForward) = self.fieldInFrontOf()
        entry = lines[self.yForward][self.xForward]
        if entry == "I":
            lines[self.yForward][self.xForward] = "."
            return True
        else:
            return False


boardSize = 8
turtle = Turtle(0, boardSize - 1)

lines = []
for _ in range(boardSize):
    line = list(input())
    lines.append(line)

encounteredBug = False
commands = list(input())
for command in commands:
    {
        "F": lambda: turtle.move(),
        "R": lambda: turtle.rotateClockwise(),
        "L": lambda: turtle.rotateCounterClockwise(),
        "X": lambda: not turtle.shoot(lines) or encounteredBug
    }[command]()

    entry = lines[turtle.y][turtle.x]
    if entry == "C" or entry == "I":
        encounteredBug = True
        break

entry = lines[turtle.y][turtle.x]
if entry == "D" and not encounteredBug:
    print("Diamond!")
else:
    print("Bug!")
