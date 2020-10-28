numberOfNumbers = int(input())

sum = 0
for _ in range(numberOfNumbers):
    illformattedNumbers = input()
    number = int(illformattedNumbers[:-1])
    exponent = int(illformattedNumbers[-1])
    sum += number ** exponent

print(sum)