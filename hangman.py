from collections import Counter

letters = Counter(input())
guessingOrder = list(input())

numberOfWrongGuess = 0
for guess in guessingOrder:
    if len(letters) == 0:
        break

    if guess in letters:
        del letters[guess]
    else:
        numberOfWrongGuess += 1

if numberOfWrongGuess < 10:
    print("WIN")
else:
    print("LOSE")
