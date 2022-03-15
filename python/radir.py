from collections import deque

numberOfCards, handLimit = list(map(int, input().split()))
cards = {}
for cardNumber in range(1, numberOfCards + 1):
    card = tuple(map(int, input().split()))
    if card not in cards:
        cards[card] = cardNumber

sequenceLengthNeeded = 3
numberOfSuits = 4
numberOfValues = 13
minNumberOfTurns = None
for suit in range(1, numberOfSuits + 1):
    sequenceLength = 0
    cardNumbers = deque()
    for value in range(1, numberOfValues + 1):
        card = (suit, value)
        if card in cards:
            sequenceLength += 1
            cardNumbers.append(cards[card])

            if sequenceLengthNeeded < sequenceLength:
                sequenceLength -= 1
                cardNumbers.popleft()

            if sequenceLengthNeeded == sequenceLength:
                numberOfTurns = max(cardNumbers)
                if minNumberOfTurns is None or numberOfTurns < minNumberOfTurns:
                    minNumberOfTurns = numberOfTurns
        else:
            sequenceLength = 0
            cardNumbers.clear()

if minNumberOfTurns is None:
    print("neibb")
else:
    numberOfTurnsNeeded = max(1, minNumberOfTurns - handLimit)
    print(numberOfTurnsNeeded)
