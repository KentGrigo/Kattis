def subtractLetters(letter1, letter2):
    asciiA = ord("a")
    asciiZ = ord("z")
    alphabetSize = asciiZ - asciiA + 1
    normalizedLetter1 = ord(letter1) - asciiA
    normalizedLetter2 = ord(letter2) - asciiA
    return chr((normalizedLetter1 - normalizedLetter2) % alphabetSize + asciiA)


keywordLength, ciphertextLength = list(map(int, input().split()))
plaintext = input()[::-1]
key = list(plaintext)
ciphertext = list(input())[::-1]
for index, cipherletter in enumerate(ciphertext):
    keyletter = key[index]
    plainletter = subtractLetters(cipherletter, keyletter)
    plaintext += plainletter
    key.append(plainletter)

plaintext = plaintext[::-1]
plaintext = plaintext[keywordLength:]
print(plaintext)
