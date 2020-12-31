def test(passwordParts, message):
    currentPasswordPart = passwordParts.pop()
    for letter in message:
        if letter == currentPasswordPart:
            if not passwordParts:
                return True
            currentPasswordPart = passwordParts.pop()
        elif letter in passwordParts:
            return False

    return False


password, message = input().split()
passwordParts = list(password)[::-1]
isValidMessage = test(passwordParts, message)
if isValidMessage:
    print("PASS")
else:
    print("FAIL")
