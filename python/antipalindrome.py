def checkPart(text, leftIndex, rightIndex):
    leftCharacter = text[leftIndex]
    rightCharacter = text[rightIndex]
    if leftCharacter != rightCharacter:
        return False
    
    return True

def check(text):
    for leftIndex in range(textLength - 2):
        result1 = checkPart(text, leftIndex, leftIndex + 1)
        result2 = checkPart(text, leftIndex, leftIndex + 2)
        if result1 or result2:
            return True

    return checkPart(text, -2, -1)


text = input().replace(' ', '').lower()
textLength = len(text)
isPalindrome = check(text)
if isPalindrome:
    print("Palindrome")
else:
    print("Anti-palindrome")
