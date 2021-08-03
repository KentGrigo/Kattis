numberOfTests = int(input())
for _ in range(numberOfTests):
    number = input()[::-1]
    sum = 0
    for cipher in number[1::2]:
        double = str(2 * int(cipher))
        for doubleCipher in double:
            sum += int(doubleCipher)

    for cipher in number[::2]:
        sum += int(cipher)

    if sum % 10 == 0:
        print("PASS")
    else:
        print("FAIL")
