numberOfImplications = int(input())
firstFail = None
conclusions = {}
for implicationNumber in range(1, numberOfImplications + 1):
    isAssumption = True
    implication = input().split()
    for term in implication:
        if term == "->":
            isAssumption = False

        if isAssumption:
            if firstFail is None and term not in conclusions:
                firstFail = implicationNumber
        else:
            conclusions[term] = True

if firstFail is None:
    print("correct")
else:
    print(firstFail)
