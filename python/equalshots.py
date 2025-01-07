def computeAlcoholContent(numberOfIngredients):
    totalAlcoholVolume = 0
    for _ in range(numberOfIngredients):
        volume, alcoholPercentage = list(map(int, input().split()))
        alcoholVolume = volume * alcoholPercentage / 100
        totalAlcoholVolume += alcoholVolume

    return totalAlcoholVolume


numberOfIngredientsInShot1, numberOfIngredientsInShot2 = list(map(int, input().split()))
totalAlcoholVolumeInShot1 = computeAlcoholContent(numberOfIngredientsInShot1)
totalAlcoholVolumeInShot2 = computeAlcoholContent(numberOfIngredientsInShot2)

epsilon = 0.00001
if totalAlcoholVolumeInShot1 - epsilon < totalAlcoholVolumeInShot2 < totalAlcoholVolumeInShot1 + epsilon:
    print("same")
else:
    print("different")
