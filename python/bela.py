data = input().split()
numberOfHands = int(data[0])
dominantSuit = data[1]
sizeOfHand = 4

def belotDominantValue(x):
    return {
        'A': 11,
        'K': 4,
        'Q': 3,
        'J': 20,
        'T': 10,
        '9': 14,
        '8': 0,
        '7': 0,
    }[x]

def belotNonDominantValue(x):
    return {
        'A': 11,
        'K': 4,
        'Q': 3,
        'J': 2,
        'T': 10,
        '9': 0,
        '8': 0,
        '7': 0,
    }[x]

totalValue = 0
for _ in range(numberOfHands):
    for _ in range(sizeOfHand):
        card = input()
        value = card[0]
        suit = card[1]

        if suit == dominantSuit:
            totalValue += belotDominantValue(value)
        else:
            totalValue += belotNonDominantValue(value)

print(totalValue)