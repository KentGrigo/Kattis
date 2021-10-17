numberOfTests = int(input())
for _ in range(numberOfTests):
    number = input()
    for reversedIndex, cipher in enumerate(reversed(number)):
        cipher = int(cipher)
        if cipher != 0:
            index = len(number) - reversedIndex - 1
            previousNumber = number[:index] + str(cipher - 1) + number[index + 1:]
            previousNumber = int(previousNumber)
            print(previousNumber)
            break
