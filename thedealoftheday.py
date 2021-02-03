def test(cards, numberOfCardsDealt):
    if not numberOfCardsDealt:
        return 1
    elif not cards:
        return 0
    else:
        skipCard = test(cards[1:], numberOfCardsDealt)
        takeCard = cards[0] * test(cards[1:], numberOfCardsDealt - 1)
        return skipCard + takeCard


cards = list(filter(lambda value: value, map(int, input().split())))
numberOfCardsDealt = int(input())
result = test(cards, numberOfCardsDealt)
print(result)
