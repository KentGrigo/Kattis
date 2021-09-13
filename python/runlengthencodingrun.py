def encode(text):
    encodedText = ""
    previousLetter = None
    count = 0
    for letter in text:
        if letter != previousLetter and previousLetter is not None:
            encodedText += previousLetter + str(count)
            count = 0

        previousLetter = letter
        count += 1

    encodedText += previousLetter + str(count)
    return encodedText

def decode(text):
    decodedText = ""
    for index in range(0, len(text), 2):
        letter = text[index]
        count = int(text[index+1])
        decodedText += letter * count

    return decodedText


encodingType, text = input().split()
if encodingType == "E":
    result = encode(text)
else:
    result = decode(text)

print(result)
