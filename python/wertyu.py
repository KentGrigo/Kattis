def convert(givenLetter, rows):
    if givenLetter == " ":
        return givenLetter

    for row in rows:
        for letterIndex, letter in enumerate(row):
            if givenLetter == letter:
                return row[letterIndex - 1]

    return None


rows = ["`1234567890-=", "QWERTYUIOP[]\\", "ASDFGHJKL;'", "ZXCVBNM,./"]
while True:
    try:
        line = input()
    except EOFError:
        break

    text = ""
    for letter in line:
        correctLetter = convert(letter, rows)
        text += correctLetter

    print(text)
