def isSpecialCharacter(letter):
    interval1Start = ord("!")
    interval1End = ord("*") + 1
    interval2Start = ord("[")
    interval2End = ord("]") + 1

    asciiValue = ord(letter)
    isInInterval1 = interval1Start <= asciiValue < interval1End
    isInInterval2 = interval2Start <= asciiValue < interval2End
    return isInInterval1 or isInInterval2


def test(numberOfInterpretations, text):
    newText = ""
    for letter in text:
        if isSpecialCharacter(letter):
            numberOfBackslashes = 2 ** numberOfInterpretations - 1
            newText += numberOfBackslashes * "\\"

        newText += letter

    return newText


while True:
    try:
        numberOfInterpretations = int(input())
        text = input()
    except EOFError:
        break

    metaText = test(numberOfInterpretations, text)
    print(metaText)
