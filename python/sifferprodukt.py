number = int(input())
while 9 < number:
    product = 1
    for cipher in str(number):
        cipher = int(cipher)
        if cipher != 0:
            product *= cipher

    number = product

print(number)
