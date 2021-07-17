def checkPassword(actualPassword, enteredPassword):
    if actualPassword == enteredPassword:
        return True
    
    firstCharacter = actualPassword[0]
    if firstCharacter.isnumeric() and actualPassword == firstCharacter + enteredPassword:
        return True

    lastCharacter = actualPassword[-1]
    if lastCharacter.isnumeric() and actualPassword == enteredPassword + lastCharacter:
        return True

    if actualPassword == enteredPassword.swapcase():
        return True

actualPassword = input()
enteredPassword = input()

isAccepted = checkPassword(actualPassword, enteredPassword)
if isAccepted:
    print("Yes")
else:
    print("No")
