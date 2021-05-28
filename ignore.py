while True:
    try:
        indexOfValidNumber = int(input())
    except EOFError:
        break

    validNumbers = [0, 1, 2, 5, 9, 8, 6]
    base = len(validNumbers)

    ciphers = []
    leftover = indexOfValidNumber
    while 0 < leftover:
        remainder = leftover % base
        leftover = leftover // base
        cipher = validNumbers[remainder]
        ciphers.append(cipher)

    result = "".join(map(str, ciphers))
    print(result)
