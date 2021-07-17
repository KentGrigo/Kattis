numberOfPhotos = int(input())
prevTime, prevDistance = list(map(int, input().split()))
maxSpeed = 0
for _ in range(numberOfPhotos - 1):
    currTime, currDistance = list(map(int, input().split()))
    diffTime = currTime - prevTime
    diffDistance = currDistance - prevDistance
    speed = diffDistance // diffTime
    maxSpeed = max(speed, maxSpeed)

    prevTime = currTime
    prevDistance = currDistance

print(maxSpeed)
