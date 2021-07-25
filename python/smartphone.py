def computerNumberOfKeypresses(target, draft):
    prefixLength = 0
    for targetLetter, draftLetter in zip(target, draft):
        if targetLetter == draftLetter:
            prefixLength += 1
        else:
            break

    numberOfDeletes = len(draft) - prefixLength
    numberOfAdditions = len(target) - prefixLength
    return numberOfDeletes + numberOfAdditions


numberOfSuggestions = 3
numberOfTests = int(input())
for _ in range(numberOfTests):
    target = input()
    text = input()

    minimumNumberOfKeypresses = computerNumberOfKeypresses(target, text)
    for _ in range(numberOfSuggestions):
        suggestion = input()
        numberOfKeypresses = 1 + computerNumberOfKeypresses(target, suggestion)
        if minimumNumberOfKeypresses is None or numberOfKeypresses < minimumNumberOfKeypresses:
            minimumNumberOfKeypresses = numberOfKeypresses

    print(minimumNumberOfKeypresses)
