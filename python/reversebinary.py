number = int(input())
reversedBinaryNumber = f'{number:0b}'[::-1]
reversedNumber = int(reversedBinaryNumber, 2)
print(reversedNumber)