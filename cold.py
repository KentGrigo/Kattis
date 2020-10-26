_ = input()
data = input().split()
temperatures = map(lambda temperature: int(temperature), data)

numberOfTemperaturesBelow0 = 0
for temperature in temperatures:
    if temperature < 0:
        numberOfTemperaturesBelow0 += 1
        
print(numberOfTemperaturesBelow0)