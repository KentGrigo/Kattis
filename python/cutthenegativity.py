numberOfCities = int(input())
outputs = []
for cityNumber1 in range(numberOfCities):
    cityNumber1 += 1
    prices = list(map(int, input().split()))
    for cityNumber2, price in enumerate(prices):
        cityNumber2 += 1
        if price != -1:
            output = f"{cityNumber1} {cityNumber2} {price}"
            outputs.append(output)

numberOfOutputs = len(outputs)
print(numberOfOutputs)
for output in outputs:
    print(output)
