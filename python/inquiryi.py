numberOfValues = int(input())

valuesSum = 0
values = []
for _ in range(numberOfValues):
    value = int(input())
    valuesSum += value
    values.append(value)

maxResult = 0
squaresSum = 0
for value in values:
    square = value ** 2
    valuesSum -= value
    squaresSum += square
    result = squaresSum * valuesSum
    maxResult = max(result, maxResult)

print(maxResult)
