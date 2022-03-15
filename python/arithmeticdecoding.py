def convert(binaryFloat):
    _, decimals = binaryFloat.split(".")
    base = 1
    result = 0
    for decimal in decimals:
        base *= 2
        if decimal == "1":
            result += 1 / base

    return result


lengthOfOriginalMessage = int(input())
probabilityA = int(input()) / 8
encodedMessage = convert(input())
low = 0
high = 1
originalMessage = ""
while len(originalMessage) < lengthOfOriginalMessage:
    split = low + probabilityA * (high - low)
    if encodedMessage < split:
        originalMessage += "A"
        high = split
    else:
        originalMessage += "B"
        low = split

print(originalMessage)
