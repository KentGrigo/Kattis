itemsForDiscount = 3
_ = int(input())
prices = list(map(int, input().split()))
prices.sort(reverse=True)
discount = 0
for price in prices[itemsForDiscount - 1::itemsForDiscount]:
    discount += price

print(discount)
