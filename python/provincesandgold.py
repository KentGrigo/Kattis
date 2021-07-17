data = input().split()

numberOfGold = int(data[0])
numberOfSilver = int(data[1])
numberOfCopper = int(data[2])

buyingPower = 3 * numberOfGold + 2 * numberOfSilver + 1 * numberOfCopper

victoryCard = ""
if 8 <= buyingPower:
    victoryCard = "Province"
elif 5 <= buyingPower:
    victoryCard = "Duchy"
elif 2 <= buyingPower:
    victoryCard = "Estate"

if 6 <= buyingPower:
    treasureCard = "Gold"
elif 3 <= buyingPower:
    treasureCard = "Silver"
else:
    treasureCard = "Copper"

if victoryCard == "":
    print(treasureCard)
else:
    print("{} or {}".format(victoryCard, treasureCard))
