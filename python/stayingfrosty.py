potionDuration = 180 # seconds
swimSpeed = 2 # block per second
distance, numberOfPotions = list(map(int, input().split()))
totalPotionDuration = numberOfPotions * potionDuration
totalSwimTime = distance / swimSpeed
if totalSwimTime <= totalPotionDuration:
    print("YES")
else:
    print("NO")
