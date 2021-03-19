def letterValue(letter):
    offsetFrom = ord("A")
    offsetTo = ord("Z") + 1
    return (ord(letter) - offsetFrom) % offsetTo

def textValue(text):
    sum = 0
    for letter in text:
        sum += letterValue(letter)

    return sum

def rotateLetter(letter, rotationValue):
    offsetFrom = ord("A")
    offsetTo = ord("Z") + 1
    rotatedLetterValue = (letterValue(letter) + rotationValue) % (offsetTo - offsetFrom) + offsetFrom
    return chr(rotatedLetterValue)

def rotate(text):
    rotationValue = textValue(text)
    rotatedText = ""
    for letter in text:
        rotatedLetter = rotateLetter(letter, rotationValue)
        rotatedText += rotatedLetter

    return rotatedText

def merge(message, key):
    mergedMessage = ""
    for messageLetter, keyLetter in zip(message, key):
        rotationValue = letterValue(keyLetter)
        mergedMessage += rotateLetter(messageLetter, rotationValue)

    return mergedMessage


drmMessage = list(input())
halfLength = len(drmMessage) // 2
encryptedMessage = drmMessage[:halfLength]
encryptedKey = drmMessage[halfLength:]

rotatedMessage = rotate(encryptedMessage)
rotatedKey = rotate(encryptedKey)

mergedMessage = merge(rotatedMessage, rotatedKey)
print(mergedMessage)
