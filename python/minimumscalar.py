numberOfTests = int(input())
for testNumber in range(1, numberOfTests + 1):
    lengthOfVectors = int(input())
    vector1 = list(map(int, input().split()))
    vector2 = list(map(int, input().split()))
    vector1.sort()
    vector2.sort(reverse=True)

    scalar = 0
    for value1, value2 in zip(vector1, vector2):
        scalar += value1 * value2

    print("Case #{}: {}".format(testNumber, scalar))
