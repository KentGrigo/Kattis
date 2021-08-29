numberOfDaysTillChristmas = 85
maximumNumberOfConsumption = int(input())
lowerBound = 1
upperBound = maximumNumberOfConsumption + 1
for dayNumber in range(1, numberOfDaysTillChristmas + 1):
    guess = (upperBound - lowerBound) // 2 + lowerBound
    question = guess * dayNumber
    print(question, flush = True)
    response = input()
    if response == "less":
        upperBound = guess
    elif response == "more":
        lowerBound = guess + 1
    else:
        break
