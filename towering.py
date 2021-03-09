def stackBoxes(boxHeights, towerHeight1, towerHeight2):
    def extendTower(tower, boxHeight):
        newTower = tower.copy()
        newTower.append(boxHeight)
        return newTower

    def helper(boxIndex, tower1, height1, tower2, height2):
        if towerHeight1 == height1 and \
            towerHeight2 == height2:
                return (tower1, tower2)
        elif len(boxHeights) <= boxIndex or \
                towerHeight1 < height1 or \
                towerHeight2 < height2:
                    return None

        boxHeight = boxHeights[boxIndex]
        results = []
        if len(tower1) < 3:
            results.append(helper(boxIndex + 1, extendTower(tower1, boxHeight), height1 + boxHeight, tower2, height2))
        if len(tower2) < 3:
            results.append(helper(boxIndex + 1, tower1, height1, extendTower(tower2, boxHeight), height2 + boxHeight))

        return next((result for result in results if result is not None), None)

    return helper(0, [], 0, [], 0)


data = list(map(int, input().split()))
boxHeights = data[0:6]
towerHeight1 = data[6]
towerHeight2 = data[7]
boxHeights.sort(reverse = True)

tower1, tower2 = stackBoxes(boxHeights, towerHeight1, towerHeight2)
towers = []
towers.extend(tower1)
towers.extend(tower2)
towers = list(map(str, towers))
print(" ".join(towers))
