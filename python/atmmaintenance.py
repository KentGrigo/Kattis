numberOfPeople, amountOfMoney = list(map(int, input().split()))
withdrawalAmounts = list(map(int, input().split()))

successfulWithdrawals = ''
for withdrawalAmount in withdrawalAmounts:
    if withdrawalAmount <= amountOfMoney:
        successfulWithdrawals += '1'
        amountOfMoney -= withdrawalAmount
    else:
        successfulWithdrawals += '0'

print(successfulWithdrawals)
