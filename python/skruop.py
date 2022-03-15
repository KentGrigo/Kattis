numberOfRequests = int(input())
volumeLevel = 7
for _ in range(numberOfRequests):
    request = input()
    if request == "Skru op!":
        volumeLevel = min(volumeLevel + 1, 10)
    else:
        volumeLevel = max(0, volumeLevel - 1)

print(volumeLevel)
