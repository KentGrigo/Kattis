import math

message = input()
startDenominator = math.floor(math.sqrt(len(message)))
for denominator in range(startDenominator, 0, -1):
    if len(message) % denominator == 0:
        width = denominator
        break

height = len(message) // width
decryptedMessage = ""
for x in range(width):
    for y in range(height):
        index = width * y + x
        decryptedMessage += message[index]

print(decryptedMessage)
