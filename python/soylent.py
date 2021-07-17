import math

caloriesPerBottle = 400
numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfCaloriesPerDay = int(input())
    numberOfBottles = int(math.ceil(numberOfCaloriesPerDay / caloriesPerBottle))
    print(numberOfBottles)
