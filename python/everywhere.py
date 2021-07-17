numberOfTests = int(input())

for _ in range(numberOfTests):
    numberOfCities = int(input())
    uniqueCities = set()
    for _ in range(numberOfCities):
        city = input()
        uniqueCities.add(city)
    print(len(uniqueCities))
