def normalize(letter):
    return {
        "B": "8",
        "G": "C", 
        "I": "1", 
        "O": "0", 
        "Q": "0", 
        "S": "5", 
        "U": "V",
        "Y": "V",
        "Z": "2"
    }.get(letter, letter)

def decimalValue(base27Digit):
    return "0123456789ACDEFHJKLMNPRTVWX".index(base27Digit)

def base27Digit(decimalValue):
    return "0123456789ACDEFHJKLMNPRTVWX"[decimalValue]

def computeCheckDigit(base27Value):
    base27Value = list(map(decimalValue, base27Value))
    decimalCheckDigit = (2 * base27Value[0]
                        + 4 * base27Value[1]
                        + 5 * base27Value[2]
                        + 7 * base27Value[3]
                        + 8 * base27Value[4]
                        + 10 * base27Value[5]
                        + 11 * base27Value[6]
                        + 13 * base27Value[7]) % 27
    return base27Digit(decimalCheckDigit)

def test(testNumber, newUcn, checkDigit):
    base27Value = list(map(normalize, list(newUcn)))
    actualCheckDigit = computeCheckDigit(base27Value)
    if actualCheckDigit != checkDigit:
        result = "Invalid"
    else:
        result = 0
        for index, digit in enumerate(base27Value[::-1]):
            result += decimalValue(digit) * 27 ** index

    print("{} {}".format(testNumber, result))


numberOfTests = int(input())
for _ in range(numberOfTests):
    data = input().split()
    testNumber = int(data[0])
    newUcn = data[1][:8]
    checkDigit = data[1][8]
    test(testNumber, newUcn, checkDigit)
