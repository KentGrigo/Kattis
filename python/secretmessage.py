import math

numberOfMessages = int(input())
for _ in range(numberOfMessages):
    message = input()
    messageLength = len(message)
    squareLength = math.ceil(math.sqrt(messageLength))
    squareSize = squareLength ** 2
    paddedMessage = message + "*" * (squareSize - messageLength)

    table = []
    for index in range(0, squareSize, squareLength):
        messageChunk = paddedMessage[index : index + squareLength]
        table.append(messageChunk)

    table = [*zip(*table[::-1])]
    secretMessage = ""
    for row in table:
        secretMessage += "".join(row).replace("*", "")

    print(secretMessage)
