numberOfCitizens = int(input())
sumOfAs = 0
for _ in range(numberOfCitizens):
    x, y = list(map(int, input().split()))
    a = y - x
    sumOfAs += a

print(sumOfAs / numberOfCitizens)
