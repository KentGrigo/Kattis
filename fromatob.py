origin, target = list(map(int, input().split()))
steps = 0
while target < origin:
    isEven = origin & 1 == 0
    if isEven:
        origin = origin // 2
    else:
        origin += 1

    steps += 1

steps += target - origin
origin = target
print(steps)
