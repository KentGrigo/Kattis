import itertools

def findSmallestHigherValue(value):
    permutations = sorted(set(itertools.permutations(value)))
    isNextValue = False
    for permutation in permutations:
        if isNextValue and permutation != value:
            return "".join(permutation)
        elif permutation == value:
            isNextValue = True

    return None


value = tuple(input())
nextHigherValue = findSmallestHigherValue(value)
if nextHigherValue is None:
    print(0)
else:
    print(nextHigherValue)
