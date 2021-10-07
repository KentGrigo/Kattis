numberOfTests = int(input())
for testNumber in range(numberOfTests):
    if testNumber:
        print("")

    menuToKnownIngredients = {}
    knownToMenuIngredients = {}
    numberOfPizzas = int(input())
    for _ in range(numberOfPizzas):
        pizzaName = input()
        _, *menuIngredients = input().split()
        _, *knownIngredients = input().split()

        for menuIngredient in menuIngredients:
            pairings = menuToKnownIngredients.get(menuIngredient, set(knownIngredients))
            pairings = set.intersection(pairings, knownIngredients)
            menuToKnownIngredients[menuIngredient] = pairings

        for knownIngredient in knownIngredients:
            pairings = knownToMenuIngredients.get(knownIngredient, set(menuIngredients))
            pairings = set.intersection(pairings, menuIngredients)
            knownToMenuIngredients[knownIngredient] = pairings

    pairs = []
    for menuIngredient, knownIngredients in menuToKnownIngredients.items():
        for knownIngredient in knownIngredients:
            menuIngredients = knownToMenuIngredients[knownIngredient]
            if menuIngredient in menuIngredients:
                pair = (menuIngredient, knownIngredient)
                pairs.append(pair)

    pairs.sort()
    for menuIngredient, knownIngredient in pairs:
        print("({}, {})".format(menuIngredient, knownIngredient))
