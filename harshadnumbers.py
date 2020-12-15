limit = int(input())

number = limit
while True:
    digits = str(number)
    sum = 0
    for digit in digits:
        sum += int(digit)
    
    if number % sum == 0:
        break
    
    number += 1

print(number)
