numberOfTest = int(input())
for testNumber in range(1, numberOfTest + 1):
    numberOfSnappers, numberOfSnaps = list(map(int, input().split()))
    binaryRepresentation = "{:b}".format(numberOfSnaps)
    relevantDigits = binaryRepresentation.zfill(numberOfSnappers)[-numberOfSnappers:]
    isBulbOn = "0" not in relevantDigits
    if isBulbOn:
        result = "ON"
    else:
        result = "OFF"

    output = "Case #{}: {}".format(testNumber, result)
    print(output)
