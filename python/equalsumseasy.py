def computeIndicesForDuplicateSums(values, numberOfValues):
    sumToValues = {}
    def helper(index, subsum, indices):
        if numberOfValues <= index:
            if indices is []:
                return None
            elif subsum in sumToValues:
                return (sumToValues[subsum], indices)
            else:
                sumToValues[subsum] = indices
                return None
        else:
            result =  helper(index + 1, subsum, indices)
            if result is not None:
                return result
            else:
                return helper(index + 1, subsum + values[index], indices + [index])

    return helper(0, 0, [])


numberOfValues = 20
numberOfCases = int(input())
for caseNumber in range(1, numberOfCases + 1):
    values = list(map(int, input().split()))
    result = computeIndicesForDuplicateSums(values, numberOfValues)
    print("Case #{}:".format(caseNumber))
    if result is None:
        print("Impossible")
    else:
        indices1, indices2 = result
        print(" ".join(map(str, map(lambda index: values[index], indices1))))
        print(" ".join(map(str, map(lambda index: values[index], indices2))))
