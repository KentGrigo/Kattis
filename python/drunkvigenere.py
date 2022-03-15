encryptedText = input()
key = input()
decryptedText = ""
isEven = True
for encryptedLetter, keyLetter in zip(encryptedText, key):
    offset = ord(keyLetter) - 65
    if isEven:
        offset *= -1

    letterIndex = (ord(encryptedLetter) - 65 + offset) % 26 + 65
    decryptedLetter = chr(letterIndex)
    decryptedText += decryptedLetter

    isEven = not isEven

print(decryptedText)
