numberOfDays = int(input())
giftsPerDay = [0]
for dayNumber in range(1, numberOfDays + 1):
    previousNumberOfGifts = giftsPerDay[dayNumber - 1]
    curretNumberOfGifts = previousNumberOfGifts + dayNumber
    giftsPerDay.append(curretNumberOfGifts)

print(giftsPerDay[numberOfDays])
print(sum(giftsPerDay))
