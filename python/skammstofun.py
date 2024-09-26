numberOfWords = input() 
words = input().split()
abbreviation = ""
for word in words:
    firstLetter = word[0]
    if firstLetter == firstLetter.capitalize():
        abbreviation += firstLetter

print(abbreviation)
