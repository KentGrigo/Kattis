text = input()
result = ''
previousLetter = ''
for letter in text:
    if previousLetter != letter:
        result += letter

    previousLetter = letter

print(result)
