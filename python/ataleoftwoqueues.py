_ = input()
waitingTimeOfLeftQueue = sum(map(int, input().split()))
waitingTimeOfRightQueue = sum(map(int, input().split()))
if waitingTimeOfLeftQueue < waitingTimeOfRightQueue:
    print("left")
elif waitingTimeOfLeftQueue == waitingTimeOfRightQueue:
    print("either")
else:
    print("right")
