import sys

numberOfFlights = int(input())
minPrice = sys.maxsize
maxPrice = 0
for _ in range(numberOfFlights):
    price = int(input())
    minPrice = min(minPrice, price)
    maxPrice = max(maxPrice, price)

personalExpense = max(0, int(minPrice - maxPrice / 2))
print(personalExpense)
