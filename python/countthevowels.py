vowels = ['A', 'E', 'I', 'O', 'U']
text = input().upper()

numberOfVowels = 0
for letter in text:
    if letter in vowels:
        numberOfVowels += 1

print(numberOfVowels)
