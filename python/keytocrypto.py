def subtractLetters(letter1, letter2):
    asciiA = ord("A")
    asciiZ = ord("Z")
    alphabetSize = asciiZ - asciiA + 1
    normalizedLetter1 = ord(letter1) - asciiA
    normalizedLetter2 = ord(letter2) - asciiA
    return chr((normalizedLetter1 - normalizedLetter2) % alphabetSize + asciiA)


ciphertext = input()
secretword = input()
key = secretword
plaintext = ""
for index, cipherletter in enumerate(ciphertext):
    keyletter = key[index]
    plainletter = subtractLetters(cipherletter, keyletter)
    plaintext += plainletter
    key += plainletter

print(plaintext)
