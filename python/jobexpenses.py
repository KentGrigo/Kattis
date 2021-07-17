numberOfTransactions = int(input())
transactions = input().split()

totalExpenses = 0
for transaction in transactions:
    transaction = int(transaction)
    if transaction < 0:
        totalExpenses += -transaction

print(totalExpenses)
