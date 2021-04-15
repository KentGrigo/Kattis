numberOfCards, secretPrediction, numberOfSteps = list(map(int, input().split()))

for _ in range(numberOfSteps):
    numberOfCardsChosen, *cardsChosen = list(map(int, input().split()))
    if secretPrediction in cardsChosen:
        print("KEEP")
    else:
        print("REMOVE")
