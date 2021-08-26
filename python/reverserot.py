alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    data = input()
    if data == "0":
        break

    numberOfRotations, text = data.split()
    numberOfRotations = int(numberOfRotations)

    text = text[::-1]
    encryptedText = ""
    for letter in text:
        index = alphabet.index(letter)
        index = (index + numberOfRotations) % len(alphabet)
        encryptedLetter = alphabet[index]
        encryptedText += encryptedLetter

    print(encryptedText, flush=True)
