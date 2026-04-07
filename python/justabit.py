bits = input()
numberOfZeros = 0
numberOfOnes = 0
for bit in bits:
    if bit == '0':
        numberOfZeros += 1
    else:
        numberOfOnes += 1

result = '{} {}'.format(numberOfZeros, numberOfOnes)
print(result)
