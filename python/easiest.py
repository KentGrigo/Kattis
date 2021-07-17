def digitSum(digits):
    sum = 0
    for digit in digits:
        sum += int(digit)

    return sum


while True:
    N = input()
    if N == "0":
        break

    digitSumOfN = digitSum(N)
    N = int(N)
    m = 11
    while True:
        product = str(N * m)
        digitSumOfProduct = digitSum(product)
        if digitSumOfN == digitSumOfProduct:
            break

        m += 1

    print(m)
