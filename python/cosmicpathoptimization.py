import math

numberOfMeasurements = int(input())
temperatures = list(map(int, input().split()))
averageTemperature = sum(temperatures) / len(temperatures)
roundedAverageTemperature = math.floor(averageTemperature)
print(roundedAverageTemperature)
