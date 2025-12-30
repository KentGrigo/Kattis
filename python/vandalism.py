initialAcronym = 'UAPC'
vandalizedAcronym = input()
missingLetters = ''
for letter in initialAcronym:
    if letter not in vandalizedAcronym:
        missingLetters += letter

print(missingLetters)
