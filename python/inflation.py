numberOfBalloons = int(input())
heliumAmounts = sorted(map(int, input().split()))
minFraction = 1.0
for balloonSize, heliumAmount in zip(range(1, numberOfBalloons + 1), heliumAmounts):
    if balloonSize < heliumAmount:
        minFraction = None
    else:
        fraction = heliumAmount / balloonSize
        if minFraction is not None:
            minFraction = min(minFraction, fraction)

if minFraction is None:
    print("impossible")
else:
    print(minFraction)
