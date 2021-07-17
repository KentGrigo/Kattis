numberOfPeriods = int(input())

totalQualityOfLife = 0
for i in range(numberOfPeriods):
    data = input().split()
    qualityOfLife = float(data[0])
    period = float(data[1])
    totalQualityOfLife += qualityOfLife * period 

print(totalQualityOfLife)