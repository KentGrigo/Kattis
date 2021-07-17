def computeWhetherAdventureIsASuccess(adventure):
    stack = []
    for item in adventure:
        if item in [money, incense, gem]:
            stack.append(item)
        elif item in [banker, trader, jeweler]:
            try:
                lastItem = stack.pop()
            except IndexError:
                return False

            if lastItem == money and item != banker or \
                lastItem == incense and item != trader or \
                lastItem == gem and item != jeweler:
                    return False
        else: # item == nothing
            pass # do nothing

    return len(stack) == 0


money = "$"
incense = "|"
gem = "*"
banker = "b"
trader = "t"
jeweler = "j"
nothing = "."
numberOfAdventures = int(input())
for _ in range(numberOfAdventures):
    adventure = list(input())
    isAdventureASuccess = computeWhetherAdventureIsASuccess(adventure)
    if isAdventureASuccess:
        print("YES")
    else:
        print("NO")
