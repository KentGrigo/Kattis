numberOfMountains = int(input())
mountainHeights = list(map(lambda height: int(height), input().split()))

currentPeak = mountainHeights[0]
currentValley = mountainHeights[0]
biggestJumpingDistance = 0
for mountainHeight in mountainHeights:
    currentValley = min(currentValley, mountainHeight)
    if currentPeak <= mountainHeight:
        prominence = currentPeak - currentValley
        biggestJumpingDistance = max(biggestJumpingDistance, prominence)

        currentPeak = mountainHeight
        currentValley = mountainHeight

    else:
        prominence = mountainHeight - currentValley
        biggestJumpingDistance = max(biggestJumpingDistance, prominence)

print(biggestJumpingDistance)