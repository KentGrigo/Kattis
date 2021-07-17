data = input().split()
priceOfCandy = int(data[0])
magnitudeOfSmallestBill = int(data[1])

smallestBill = 10 ** magnitudeOfSmallestBill
roundedPrice = round(priceOfCandy / smallestBill) * smallestBill
print(roundedPrice)
