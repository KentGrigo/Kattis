def test(numerator, denominator):
    wholeNumber = numerator // denominator
    remainder = numerator % denominator
    print("{} {} / {}".format(wholeNumber, remainder, denominator))


while True:
    fraction = input().split()
    numerator = int(fraction[0])
    denominator = int(fraction[1])
    if numerator == 0 and denominator == 0:
        break

    test(numerator, denominator)
