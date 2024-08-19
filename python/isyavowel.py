text = input()
vowels = ['a', 'e', 'i', 'o', 'u']

numberOfVowelsExcludingY = 0
numberOfYs = 0
for letter in text:
    if letter in vowels:
        numberOfVowelsExcludingY += 1
    elif letter == 'y':
        numberOfYs += 1

numberOfVowelsIncludingY = numberOfVowelsExcludingY + numberOfYs
print(f"{numberOfVowelsExcludingY} {numberOfVowelsIncludingY}")
