windSpeed = int(input())
numberOfRoads = int(input())
for _ in range(numberOfRoads):
    (roadName, maxWindSpeed) = input().split()
    maxWindSpeed = int(maxWindSpeed)
    if windSpeed <= maxWindSpeed:
        print(roadName, "opin")
    else:
        print(roadName, "lokud")
