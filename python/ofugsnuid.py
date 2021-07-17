numberOfNumbers = int(input())

numbers = []
for _ in range(numberOfNumbers):
    number = int(input())
    numbers.append(number)

for number in numbers[::-1]:
    print(number)
