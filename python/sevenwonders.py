import math

cards = input()

numberOfTablets = 0
numberOfCompasses = 0
numberOfGears = 0
for card in cards:
    if (card == 'T'):
        numberOfTablets += 1
    elif (card == 'C'):
        numberOfCompasses += 1
    elif (card == 'G'):
        numberOfGears += 1
    else:
        exit("{} is not supported".format(card))

numberOfSets = min(numberOfTablets, min(numberOfCompasses, numberOfGears))
score = numberOfTablets ** 2 + numberOfCompasses ** 2 + numberOfGears ** 2 + 7 * numberOfSets
print(score)