period1, period2, patience = list(map(int, input().split()))
lamp1 = period1
lamp2 = period2
while lamp1 != lamp2 and lamp1 <= patience and lamp2 <= patience:
    if lamp1 < lamp2:
        lamp1 += period1
    else:
        lamp2 += period2

if lamp1 == lamp2 and lamp1 <= patience and lamp2 <= patience:
    print("yes")
else:
    print("no")
