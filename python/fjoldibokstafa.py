text = input()
numberOfCharacters = 0
for character in text:
    if character.isalpha():
        numberOfCharacters += 1

print(numberOfCharacters)
