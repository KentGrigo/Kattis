password1 = input()
password2 = input()

numberOfCombinations = 1
for digit1, digit2 in zip(password1, password2):
    if digit1 != digit2:
        numberOfCombinations *= 2

print(numberOfCombinations)
