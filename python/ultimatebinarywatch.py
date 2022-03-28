ciphers = map(int, list(input()))
binaries = list(map(lambda cipher: '{0:04b}'.format(cipher), ciphers))
for column in range(4):
    output = ''
    for index, binary in enumerate(binaries):
        if index == 2:
            output += '   '
        elif index != 0:
            output += ' '

        bit = binary[column]
        if bit == '1':
            symbol = '*'
        else:
            symbol = '.'

        output += symbol

    print(output)
