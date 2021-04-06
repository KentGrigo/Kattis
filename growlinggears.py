# Given parabola: T = -aR^2 + bR + c
# Differential: dT / dR = -2aR + b
# Solving R for dT / dR = 0: R = b / 2a

numberOfTests = int(input())
for _ in range(numberOfTests):
    maxTorque = 0
    gearNumberWithMaxTorque = None
    numberOfGears = int(input())
    for gearNumber in range(1, numberOfGears + 1):
        a, b, c = list(map(int, input().split()))
        peakR = b / (2 * a)
        torqueAtPeak = -a * peakR ** 2 + b * peakR + c
        if maxTorque < torqueAtPeak:
            maxTorque = torqueAtPeak
            gearNumberWithMaxTorque = gearNumber

    print(gearNumberWithMaxTorque)
