memoization = {}
def helperMemoized(targetLetters, letters, startTargetIndex, startIndex):
    if memoization.get((startTargetIndex, startIndex)) == None:
        memoization[(startTargetIndex, startIndex)] = helper(targetLetters, letters, startTargetIndex, startIndex)
    return memoization.get((startTargetIndex, startIndex))

def helper(targetLetters, letters, startTargetIndex, startIndex):
    if len(targetLetters) <= startTargetIndex:
        return 1

    result = 0
    for index in range(startIndex, len(letters)):
        letter = letters[index]
        targetLetter = targetLetters[startTargetIndex]
        if targetLetter == letter:
            result += helperMemoized(targetLetters, letters, startTargetIndex + 1, index + 1)

    return result

def test(targetText, text):
    memoization.clear()
    targetLetters = list(targetText)
    letters = list(text)
    return helperMemoized(targetLetters, letters, 0, 0)


numberOfTests = int(input())
targetText = "welcome to code jam"
for testNumber in range(1, numberOfTests + 1):
    text = input()
    result = test(targetText, text) % 10000
    print("Case #{}: {:04d}".format(testNumber, result))
