numberOfProblems = int(input())
numberOfExcludedProblems = 0
for _ in range(numberOfProblems):
    rating = int(input())
    isOdd = rating % 2 != 0
    if isOdd:
        numberOfExcludedProblems += 1

print(numberOfExcludedProblems)
