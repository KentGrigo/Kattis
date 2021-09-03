numberOfRecipes = int(input())
for recipeNumber in range(1, numberOfRecipes + 1):
    numberOfIngredients, numberOfPortions, numberOfDesiredPortions = list(map(int, input().split()))
    ingredientsAndPercentages = []
    for _ in range(numberOfIngredients):
        ingredient, amount, percentage = input().split()
        amount = float(amount)
        percentage = float(percentage)
        ingredientsAndPercentages.append((ingredient, percentage))
        if percentage == 100.0:
            mainAmount = amount * numberOfDesiredPortions / numberOfPortions

    print("Recipe # {}".format(recipeNumber))
    for ingredient, percentage in ingredientsAndPercentages:
        amount = mainAmount * percentage / 100
        print("{} {}".format(ingredient, amount))

    print("----------------------------------------")



