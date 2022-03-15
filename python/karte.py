def checkDeck(deck):
    cards = {}
    for index in range(0, len(deck), 3):
        card = deck[index : index + 3]
        suit = card[0]
        value = int(card[1:])
        if (suit, value) in cards:
            return None

        cards[(suit, value)] = True

    missingCardsForSuits = []
    suits = ["P", "K", "H", "T"]
    values = list(range(1, 13 + 1))
    for suit in suits:
        numberOfMissingCards = 0
        for value in values:
            if (suit, value) not in cards:
                numberOfMissingCards += 1

        missingCardsForSuits.append(numberOfMissingCards)

    return missingCardsForSuits


deck = input()
result = checkDeck(deck)
if result is None:
    print("GRESKA")
else:
    output = " ".join(map(str, result))
    print(output)
