transactionFeeOnMonnei = int(input())
transactionFeeOnFjee = int(input())
transactionFeeOnDolladollabilljoll = int(input())
minimumTransactionFee = min(transactionFeeOnMonnei, transactionFeeOnFjee, transactionFeeOnDolladollabilljoll)
if minimumTransactionFee == transactionFeeOnMonnei:
    print("Monnei") 
elif minimumTransactionFee == transactionFeeOnFjee:
    print("Fjee") 
else:
    print("Dolladollabilljoll") 
