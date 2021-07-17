def test(caseNumber):
    numberOfGuests = int(input())
    invitationCodes = list(map(lambda code: int(code), input().split()))
    foundNumbers = {}
    for code in invitationCodes:
        foundNumbers[code] = foundNumbers.get(code, 0) + 1

    for code, occurrences in foundNumbers.items():
        if occurrences == 1:
            print("Case #{}: {}".format(caseNumber, code))

numberOfCases = int(input())
for caseNumber in range(1, numberOfCases + 1):
    test(caseNumber)
