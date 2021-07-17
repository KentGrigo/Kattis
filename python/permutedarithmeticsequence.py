def isArithmeticSequence(sequence):
    difference = sequence[1] - sequence[0]
    for value1, value2 in zip(sequence[:-1], sequence[1:]):
        if value2 - value1 != difference:
            return False

    return True


numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfNumbers, *sequence = list(map(int, input().split()))
    if isArithmeticSequence(sequence):
        print("arithmetic")
    elif isArithmeticSequence(sorted(sequence)):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")
