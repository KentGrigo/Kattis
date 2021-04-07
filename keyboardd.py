correctText = input()
wrongText = input()

stickyKeys = set()
correctTextIndex = 0
wrongTextIndex = 0
while correctTextIndex < len(correctText) and wrongTextIndex < len(wrongText):
    correctLetter = correctText[correctTextIndex]
    wrongLetter = wrongText[wrongTextIndex]
    if correctLetter != wrongLetter:
        stickyKeys.add(wrongLetter)
        wrongTextIndex += 1
    else:
        correctTextIndex += 1
        wrongTextIndex += 1

while wrongTextIndex < len(wrongText):
    wrongLetter = wrongText[wrongTextIndex]
    stickyKeys.add(wrongLetter)
    wrongTextIndex += 1

print("".join(stickyKeys))
