numberOfTransactions = int(input())
initialBalance = 0
balance = 0
for _ in range(numberOfTransactions):
    transaction = int(input())
    balance += transaction
    initialBalance = max(initialBalance, -balance)

print(initialBalance)
