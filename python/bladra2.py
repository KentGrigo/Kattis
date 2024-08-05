velocity, acceleration, duration = list(map(int, input().split()))
distance = velocity * duration + 1/2 * acceleration * duration * duration
print(distance)
