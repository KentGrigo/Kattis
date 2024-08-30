year = int(input())
initialPrice = 1000
yearlyIncrement = 100
lastYearWithFlatRate = 2020

if year <= lastYearWithFlatRate:
    print(initialPrice)
else:
    numberOfIncrements = year - lastYearWithFlatRate
    newPrice = initialPrice + yearlyIncrement * numberOfIncrements
    print(newPrice)
