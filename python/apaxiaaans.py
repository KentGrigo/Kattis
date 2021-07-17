name = input()

previousLetter = ""
shortenedName = ""
for letter in name:
    if letter != previousLetter:
        shortenedName += letter
    previousLetter = letter

print(shortenedName)
