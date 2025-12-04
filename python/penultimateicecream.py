numberOfIceCream = int(input())
iceCreamPrices = sorted(map(int, input().split()))
priceOfChosenIceCream = iceCreamPrices[numberOfIceCream - 2]
print(priceOfChosenIceCream)
