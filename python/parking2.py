numberOfTests = int(input())

for _ in range(numberOfTests):
    numberOfStores = int(input())
    storeLocations = list(map(lambda location: int(location), input().split()))
    firstStore = min(storeLocations)
    lastStore = max(storeLocations)
    walkingDistance = 2 * (lastStore - firstStore)
    print(walkingDistance)