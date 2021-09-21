numberOfCommercialBreaks, commercialPrice = list(map(int, input().split()))
numberOfListenersPerCommercialBreaks = list(map(int, input().split()))
incomePerListener = 1
maxIncome = 0
previousAccumulatedIncome = 0
for numberOfListeners in numberOfListenersPerCommercialBreaks:
    income = numberOfListeners * incomePerListener - commercialPrice
    accumulatedIncome = max(0, previousAccumulatedIncome + income)
    maxIncome = max(maxIncome, accumulatedIncome)
    previousAccumulatedIncome = accumulatedIncome

print(maxIncome)
