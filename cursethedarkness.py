import math

candleLightRadius = 8 # meter

def distance(x1, y1, x2, y2):
    xDifference = x1 - x2
    yDifference = y1 - y2
    return math.sqrt(xDifference ** 2 + yDifference ** 2)

def test():
    bookLocation = input().split()
    bookX = float(bookLocation[0])
    bookY = float(bookLocation[1])
    numberOfCandles = int(input())
    candleLocations = []
    for _ in range(numberOfCandles):
        candleLocation = input()
        candleLocations.append(candleLocation)

    for candleLocation in candleLocations:
        candleLocation = candleLocation.split()
        candleX = float(candleLocation[0])
        candleY = float(candleLocation[1])

        distanceToCandle = distance(bookX, bookY, candleX, candleY)
        if distanceToCandle <= candleLightRadius:
            return True

    return False

numberOfTests = int(input())
for _ in range(numberOfTests):
    willCandleGiveLight = test()
    if willCandleGiveLight:
        print("light a candle")
    else:
        print("curse the darkness")
