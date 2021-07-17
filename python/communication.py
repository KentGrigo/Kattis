def decimalToBinary(decimal):
    return "{:08b}".format(decimal)

def binaryToDecimal(binary):
    return int(str(binary), 2)

def encode(number):
    return number ^ (number << 1) % 256

def decode(number):
    binaryNumber = decimalToBinary(int(number))
    originalNumber = ""
    previousOriginalDigit = 0
    for binaryDigit in binaryNumber[::-1]:
        originalDigit = int(binaryDigit) ^ previousOriginalDigit
        originalNumber = str(originalDigit) + originalNumber
        previousOriginalDigit = originalDigit

    return binaryToDecimal(originalNumber)


numberOfNumbers = int(input())
numbers = input().split()

originalNumbers = []
for number in numbers:
    originalNumber = str(decode(number))
    originalNumbers.append(originalNumber)

print(" ".join(originalNumbers))
