numberOfTrips = int(input())
trips = {}
for _ in range(numberOfTrips):
    country, year = input().split()
    year = int(year)
    years = trips.get(country, [])
    years.append(year)
    trips[country] = years

for years in trips.values():
    years.sort()

numberOfQueries = int(input())
for _ in range(numberOfQueries):
    country, index = input().split()
    index = int(index) - 1
    years = trips[country]
    year = years[index]
    print(year)
