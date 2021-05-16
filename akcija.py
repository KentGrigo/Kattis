numberOfBooks = int(input())
bookPrices = []
for _ in range(numberOfBooks):
    bookPrice = int(input())
    bookPrices.append(bookPrice)

totalPrice = 0
bookPrices.sort()
bookGroup = []
while bookPrices:
    bookPrice = bookPrices.pop()
    bookGroup.append(bookPrice)
    if len(bookGroup) == 3:
        totalPrice += sum(bookGroup) - min(bookGroup)
        bookGroup = []

if 0 < len(bookGroup):
    totalPrice += sum(bookGroup)
    bookGroup = []

print(totalPrice)
