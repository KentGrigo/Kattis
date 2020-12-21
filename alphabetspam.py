text = input()

total = len(text)
numberOfWhitespaces = 0
numberOfLowercaseLetters = 0
numberOfUppercaseLetters = 0
numberOfSymbols = 0
for symbol in text:
    if symbol == "_":
        numberOfWhitespaces += 1
    elif symbol.islower():
        numberOfLowercaseLetters += 1
    elif symbol.isupper():
        numberOfUppercaseLetters += 1
    else:
        numberOfSymbols += 1

print(numberOfWhitespaces / total)
print(numberOfLowercaseLetters / total)
print(numberOfUppercaseLetters / total)
print(numberOfSymbols / total)
