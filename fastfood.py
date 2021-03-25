def computeNumberOfTimesPrizeCanBeCollected(stickers, requiredStickerTypes):
    numberOfMinimumSticker = 100
    for requiredStickerType in requiredStickerTypes:
        numberOfRequiredStickerType = stickers[requiredStickerType - 1]
        numberOfMinimumSticker = min(numberOfRequiredStickerType, numberOfMinimumSticker)

    return numberOfMinimumSticker

def test(stickers, prizePool):
    collected = 0
    for prize, requiredStickerTypes in prizePool:
        numberOfTimesPrizeCanBeCollected = computeNumberOfTimesPrizeCanBeCollected(stickers, requiredStickerTypes)
        collected += prize * numberOfTimesPrizeCanBeCollected

    return collected


numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfPrizes, numberOfStickerTypes = list(map(int, input().split()))
    prizePool = []
    for _ in range(numberOfPrizes):
        _, *requiredStickerTypes, prize = list(map(int, input().split()))
        prizePool.append((prize, requiredStickerTypes))

    stickers = list(map(int, input().split()))
    collected = test(stickers, prizePool)
    print(collected)
