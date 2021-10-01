numberOfProblems, numberOfTests = list(map(int, input().split()))
numberOfSolvedProblems = 0
for _ in range(numberOfProblems):
    handledAllData = True
    for _ in range(numberOfTests):
        data = input()
        lowercaseFirstLetter = data[0].lower() + data[1:]
        isDataHandled = data.lower() == lowercaseFirstLetter
        handledAllData = handledAllData and isDataHandled

    if handledAllData:
        numberOfSolvedProblems += 1

print(numberOfSolvedProblems)
