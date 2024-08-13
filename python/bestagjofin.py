numberOfGifts = int(input())

highestGiftValue = -1
bestGiftGiver = ""
for _ in range(numberOfGifts):
    giftGiver, giftValue = input().split()
    giftValue = int(giftValue)
    if highestGiftValue < giftValue:
        bestGiftGiver = giftGiver
        highestGiftValue = giftValue

print(bestGiftGiver)
