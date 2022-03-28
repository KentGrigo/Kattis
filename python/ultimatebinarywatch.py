ciphers = map(int, list(input()))
binaries = list(map(lambda cipher: '{0:04b}'.format(cipher), ciphers))
for column in range(4):
    for index, binary in enumerate(binaries):
        if index == 2:
            print('   ', end='')
        elif index != 0:
            print(' ', end='')

        bit = binary[column]
        if bit == '1':
            symbol = '*'
        else:
            symbol = '.'

        print(symbol, end='')

    print()
