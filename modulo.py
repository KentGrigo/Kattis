numberOfNumbers = 10
dividend = 42

uniqueRemainders = set()
for _ in range(numberOfNumbers):
    number = int(input())
    remainder = number % dividend
    uniqueRemainders.add(remainder)

print(len(uniqueRemainders))