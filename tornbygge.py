numberOfBricks = int(input())
widths = list(map(int, input().split()))

numberOfTowers = 0
previousWidth = None
for width in widths:
    if previousWidth is None or previousWidth < width:
        numberOfTowers += 1

    previousWidth = width

print(numberOfTowers)
