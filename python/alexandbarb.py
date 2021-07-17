data = input().split()
numberOfCards = int(data[0])
minimumTake = int(data[1])
maximumTake = int(data[2])

relevantNumberOfCards = numberOfCards % (minimumTake + maximumTake)
willAlexWin = minimumTake <= relevantNumberOfCards

if willAlexWin:
    print("Alex")
else:
    print("Barb")
