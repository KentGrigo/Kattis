requiredAmount = int(input())
glassAmount = 1
bottleAmount = 7

if requiredAmount == 0 or requiredAmount == 7:
    usedAmount = requiredAmount
else:
    usedAmount = requiredAmount + 1

print(usedAmount)
