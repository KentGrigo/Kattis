numberOfNumbers = int(input())
hasMissingNumbers = False
previousNumber = 0
for _ in range(numberOfNumbers):
    currentNumber = int(input())
    for missingNumber in range(previousNumber + 1, currentNumber):
        hasMissingNumbers = True
        print(missingNumber)

    previousNumber = currentNumber

if not hasMissingNumbers:
    print("good job")
