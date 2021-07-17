data = input().split()
numberOfObstacles = int(data[0])
numberOfObservedObstacles = int(data[1])

observedObstacles = set()
for _ in range(numberOfObservedObstacles):
    observedObstacle = int(input())
    if observedObstacle < numberOfObstacles:
        observedObstacles.add(observedObstacle)
observedObstacles = sorted(observedObstacles)

lastObserved = -1
for observedObstacle in observedObstacles:
    for unobservedObstacle in range(lastObserved + 1, observedObstacle):
        print(unobservedObstacle)
    lastObserved = observedObstacle

for unobservedObstacle in range(lastObserved + 1, numberOfObstacles):
    print(unobservedObstacle)

print("Mario got {} of the dangerous obstacles.".format(len(observedObstacles)))
