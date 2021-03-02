def getEntry(treasureMap, playerX, playerY):
    return treasureMap[playerY][playerX]

def setEntry(treasureMap, playerX, playerY, value):
    treasureMap[playerY][playerX] = value

def hasNearbyTraps(treasureMap, playerX, playerY):
    return getEntry(treasureMap, playerX - 1, playerY) == "T" or \
            getEntry(treasureMap, playerX + 1, playerY) == "T" or \
            getEntry(treasureMap, playerX, playerY - 1) == "T" or \
            getEntry(treasureMap, playerX, playerY + 1) == "T"

def traverse(treasureMap, playerX, playerY):
    """
    P means player
    T means trap
    # means wall
    . means floor
    G means gold
    M means marked/traversed
    """
    numberOfGold = 0
    entry = getEntry(treasureMap, playerX, playerY)
    if entry in ["M", "#", "T"]:
        return 0
    elif entry in [".", "P"]:
        setEntry(treasureMap, playerX, playerY, "M")
    elif entry == "G":
        setEntry(treasureMap, playerX, playerY, "M")
        numberOfGold += 1

    if not hasNearbyTraps(treasureMap, playerX, playerY):
        numberOfGold += traverse(treasureMap, playerX - 1, playerY)
        numberOfGold += traverse(treasureMap, playerX + 1, playerY)
        numberOfGold += traverse(treasureMap, playerX, playerY - 1)
        numberOfGold += traverse(treasureMap, playerX, playerY + 1)

    return numberOfGold


width, height = list(map(int, input().split()))
treasureMap = []
for y in range(height):
    row = list(input())
    treasureMap.append(row)
    try: 
        playerX = row.index("P")
        playerY = y
    except ValueError:
        pass

reachableGold = traverse(treasureMap, playerX, playerY)
print(reachableGold)
