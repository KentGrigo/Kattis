numberOfCards = int(input())
cards = sorted(map(int, input().split()))

score = 0
previousCard = None
for currentCard in cards:
    if previousCard is None or previousCard + 1 != currentCard:
        score += currentCard

    previousCard = currentCard

print(score)
