import math
from collections import deque

requestLength = 1000
numberOfRequests, numberOfRequestsPerServer = list(map(int, input().split()))
numberOfServers = 0
currentRequests = deque()
for _ in range(numberOfRequests):
    startTimeOfRequest = int(input())
    endTimeOfRequest = startTimeOfRequest + requestLength
    while currentRequests and currentRequests[0] <= startTimeOfRequest:
        currentRequests.popleft()

    currentRequests.append(endTimeOfRequest)
    numberOfServersNeeded = int(math.ceil(len(currentRequests) / numberOfRequestsPerServer))
    numberOfServers = max(numberOfServers, numberOfServersNeeded)

print(numberOfServers)
