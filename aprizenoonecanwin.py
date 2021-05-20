numberOfItems, prizeCost = list(map(int, input().split()))
prizes = list(map(int, input().split()))
prizes.sort()
numberOfMarkedItems = 1
for prize1, prize2 in zip(prizes[:-1], prizes[1:]):
    if prizeCost < prize1 + prize2:
        break
    else:
        numberOfMarkedItems += 1

print(numberOfMarkedItems)
