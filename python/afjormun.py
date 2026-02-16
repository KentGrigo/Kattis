numberOfSentences = int(input())
for _ in range(numberOfSentences):
    sentence = input()
    unmemedSentence = sentence[0].upper() + sentence[1:].lower()
    print(unmemedSentence)
