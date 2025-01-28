text = input()
correctText = ""
previousLetter = None
for letter in text:
    if letter != previousLetter:
        correctText += letter

    previousLetter = letter

print(correctText)
