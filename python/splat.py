import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        xDifference = self.x - other.x
        yDifference = self.y - other.y
        return math.sqrt(xDifference ** 2 + yDifference ** 2)

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def collide(self, point):
        distanceFromCenter = self.center.distance(point)
        return distanceFromCenter <= self.radius

class ColoredCircle:
    def __init__(self, circle, color):
        self.circle = circle
        self.color = color

    def collide(self, point):
        return self.circle.collide(point)

numberOfPaintings = int(input())
for _ in range(numberOfPaintings):
    paintedCircles = []
    numberOfPaintDrops = int(input())
    for _ in range(numberOfPaintDrops):
        paint = input().split()
        x = float(paint[0])
        y = float(paint[1])
        volume = float(paint[2])
        color = paint[3]
        radius = math.sqrt(volume / math.pi)
        paintedCircle = ColoredCircle(Circle(Point(x, y), radius), color)
        paintedCircles.append(paintedCircle)

    numberOfQueries = int(input())
    for _ in range(numberOfQueries):
        query = input().split()
        x = float(query[0])
        y = float(query[1])
        queryPoint = Point(x, y)
        queriedColor = "white"
        for paintedCircle in paintedCircles[::-1]:
            if paintedCircle.collide(queryPoint):
                queriedColor = paintedCircle.color
                break

        print(queriedColor)
