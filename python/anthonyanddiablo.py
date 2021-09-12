import math

neededAreaSize, gotFenceLength = list(map(float, input().split()))
neededFenceLength = 2 * math.sqrt(math.pi * neededAreaSize)
if gotFenceLength < neededFenceLength:
    print("Need more materials!")
else:
    print("Diablo is happy!")
