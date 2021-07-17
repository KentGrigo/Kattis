def test(numberOfNames):
    beginningNames = []
    endingNames = []
    isBeginningName = True
    for _ in range(numberOfNames):
        name = input()
        if isBeginningName:
            beginningNames.append(name)
        else:
            endingNames.append(name)
        
        isBeginningName = not isBeginningName

    for name in beginningNames:
        print(name)

    for name in endingNames[::-1]:
        print(name)


caseNumber = 1
while True:
    numberOfNames = int(input())
    if numberOfNames == 0:
        break

    print("SET {}".format(caseNumber))
    test(numberOfNames)
    caseNumber += 1
