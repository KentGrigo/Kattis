numberOfTests = int(input())

for _ in range(numberOfTests):
    data = input().split()
    powerStrips = list(map(lambda entry: int(entry), data[1:]))
    numberOfOutlets = sum(powerStrips)
    numberOfPowerStrips = len(powerStrips)
    numberOfUsableOutlets = numberOfOutlets - numberOfPowerStrips + 1
    print(numberOfUsableOutlets)