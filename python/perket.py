def computeMinimumDifference(ingredients):
    def helper(index, totalSourness, totalBitterness, numberOfAddedIngredients):
        if len(ingredients) <= index:
            if numberOfAddedIngredients == 0:
                return maxValue
            else:
                return abs(totalSourness - totalBitterness)
        else:
            sourness, bitterness = ingredients[index]
            result1 = helper(index + 1,
                             totalSourness,
                             totalBitterness,
                             numberOfAddedIngredients
            )
            result2 = helper(index + 1, 
                             totalSourness * sourness,
                             totalBitterness + bitterness,
                             numberOfAddedIngredients + 1
            )
            return min(result1, result2)

    return helper(0, 1, 0, 0)


maxValue = 1000000000
numberOfIngredients = int(input())
ingredients = []
for _ in range(numberOfIngredients):
    sourness, bitterness = list(map(int, input().split()))
    ingredients.append((sourness, bitterness))

minimumDifference = computeMinimumDifference(ingredients)
print(minimumDifference)
