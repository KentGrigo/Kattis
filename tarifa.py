availableMbPerMonth = int(input())
numberOfMonths = int(input())

totalAvailable = 0
totalSpent = 0
for _ in range(numberOfMonths):
    usedMbs = int(input())
    totalSpent += usedMbs
    totalAvailable += availableMbPerMonth

totalAvailable += availableMbPerMonth
leftover = totalAvailable - totalSpent 
print(leftover)
