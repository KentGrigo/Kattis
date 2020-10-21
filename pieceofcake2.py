data = input().split()
length = int(data[0])
horizontalDistance = int(data[1])
verticalDistance = int(data[2])
thickness = 4

largestHorizontal = max(horizontalDistance, length - horizontalDistance)
largestVertical = max(verticalDistance, length - verticalDistance)
largestVolume = largestHorizontal * largestVertical * thickness

print(largestVolume)