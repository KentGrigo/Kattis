numberOfEvents = int(input())
times = {}
for _ in range(numberOfEvents):
    startTime, endTime = list(map(int, input().split()))
    for time in range(startTime, endTime + 1):
        times[time] = True

print(len(times))
