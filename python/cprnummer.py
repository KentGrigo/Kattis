cpr = input()
ciphers = map(int, cpr[:6] + cpr[7:])
terms = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
result = 0
for term, cipher in zip(terms, ciphers):
    result += term * cipher

isDivisible = result % 11 == 0
if isDivisible:
    print(1)
else:
    print(0)
