def checkPart(text, leftIndex, rightIndex):
    width = rightIndex - leftIndex
    for offset in range(width):
        leftCharacter = text[leftIndex + offset]
        rightCharacter = text[rightIndex - offset]
        if leftCharacter != rightCharacter:
            return False
        
    return True

def check(text):
    for leftIndex in range(textLength):
        for rightIndex in range(leftIndex + 1, textLength):
            result = checkPart(text, leftIndex, rightIndex)
            if result:
                return True
    
    return False


text = input().replace(' ', '').lower()
textLength = len(text)
isPalindrome = check(text)
if isPalindrome:
    print("Palindrome")
else:
    print("Anti-palindrome")
