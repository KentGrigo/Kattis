numberOfTests = int(input())

def sum(limit):
    return limit * (limit + 1) // 2

# lowerLimit inclusive
# upperLimit inclusive
def sumInterval(lowerLimit, upperLimit):
    return sum(upperLimit) - sum(lowerLimit - 1)

memoization = {}
def solveMemoized(mailBoxes, fireCrackerLowerLimit, fireCrackerHigherLimit):
    if memoization.get((mailBoxes, fireCrackerLowerLimit, fireCrackerHigherLimit)) == None:
        memoization[(mailBoxes, fireCrackerLowerLimit, fireCrackerHigherLimit)] = solve(mailBoxes, fireCrackerLowerLimit, fireCrackerHigherLimit)
    return memoization.get((mailBoxes, fireCrackerLowerLimit, fireCrackerHigherLimit))
    
def solve(mailBoxes, fireCrackerLowerLimit, fireCrackerUpperLimit):
    if mailBoxes == 1:
        return sumInterval(fireCrackerLowerLimit, fireCrackerUpperLimit)
    elif fireCrackerUpperLimit < fireCrackerLowerLimit:
        return sum(fireCrackerUpperLimit)
    else:
        maxSum = sumInterval(fireCrackerLowerLimit, fireCrackerUpperLimit)
        minimumSum = maxSum
        difference = fireCrackerUpperLimit - fireCrackerLowerLimit
        start = fireCrackerLowerLimit
        end = fireCrackerUpperLimit - difference // 8
        for fireCrackerStart in range(start, end):
                lowerInterval = solveMemoized(mailBoxes - 1, fireCrackerLowerLimit, fireCrackerStart - 1)
                upperInterval = solveMemoized(mailBoxes, fireCrackerStart + 1, fireCrackerUpperLimit)
                scenario1 = fireCrackerStart + upperInterval
                scenario2 = fireCrackerStart + lowerInterval
                fireCrackersNeeded = max(scenario1, scenario2)
                minimumSum = min(minimumSum, fireCrackersNeeded)
        return minimumSum

for _ in range(numberOfTests):
    data = input().split()
    numberOfMailboxes = int(data[0])
    fireCrackerLimit = int(data[1])

    minimumSum = solveMemoized(numberOfMailboxes, 1, fireCrackerLimit)
    print(minimumSum)
