def computeCombination(values):
    def helper(index, sum, numberOfDwarves):
        if sum == 100 and numberOfDwarves == 7:
            return []

        if len(values) <= index or 100 < sum or 7 < numberOfDwarves:
            return None

        branch1 = helper(index + 1, sum, numberOfDwarves)
        if branch1 is not None:
            return branch1
        else:
            dwarfValue = values[index]
            branch2 = helper(index + 1, sum + dwarfValue, numberOfDwarves + 1)
            if branch2 is not None:
                branch2.append(dwarfValue)
                return branch2
            else:
                return None

    return helper(0, 0, 0)


numberOfDwarves = 9
dwarfValues = []
for _ in range(numberOfDwarves):
    dwarfValue = int(input())
    dwarfValues.append(dwarfValue)

correctCombination = computeCombination(dwarfValues)
for dwarfValue in reversed(correctCombination):
    print(dwarfValue)
