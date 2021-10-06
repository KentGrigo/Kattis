numbers = sorted(map(int, input().split()))

difference1 = numbers[1] - numbers[0]
difference2 = numbers[2] - numbers[1]
minDifference = min(difference1, difference2)

missingNumber = None
for number1, number2 in zip(numbers[:-1], numbers[1:]):
    difference = number2 - number1
    if difference != minDifference:
        missingNumber = number1 + minDifference
        break

if missingNumber is None:
    missingNumber = number2 + minDifference

print(missingNumber)
