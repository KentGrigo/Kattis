gcwr, truckWeight, numberOfItems = map(int, input().split())
totalItemWeight = sum(map(int, input().split()))
trailerWeight = (gcwr - truckWeight) * 0.9 - totalItemWeight
print(int(trailerWeight))
