cipherText = input()
targetText = "PER" * (len(cipherText) // 3)
difference = 0
for cipherLetter, targetLetter in zip(cipherText, targetText):
    if cipherLetter != targetLetter:
        difference += 1

print(difference)
