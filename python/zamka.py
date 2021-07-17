lowerLimit = int(input())
higherLimit = int(input())
targetSum = int(input())

def digitSum(number):
    textNumber = str(number)
    digitSum = 0
    for textDigit in textNumber:
        digit = int(textDigit)
        digitSum += digit
    return digitSum

lowerMatch = lowerLimit
while digitSum(lowerMatch) != targetSum:
    lowerMatch += 1

higherMatch = higherLimit
while digitSum(higherMatch) != targetSum:
    higherMatch -= 1

print(lowerMatch)
print(higherMatch)