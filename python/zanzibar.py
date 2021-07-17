numberOfTests = int(input())

for _ in range(numberOfTests):
    data = input().split()
    populations = list(map(lambda population: int(population), data[:-1]))

    prevPopulation = 1
    totalImported = 0
    for population in populations:
        numberOfImported = max(0, population - 2 * prevPopulation)
        totalImported += numberOfImported
        prevPopulation = population
    print(totalImported)