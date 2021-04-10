ciphertext = input()
plaintext = ""
skip = 0
for letter in ciphertext:
    if 0 < skip:
        skip -= 1
        continue

    if letter in "aeiou":
        skip = 2

    plaintext += letter

print(plaintext)
