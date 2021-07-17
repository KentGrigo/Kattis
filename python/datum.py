from datetime import date

data = input().split()
day = int(data[0])
month = int(data[1])

givenDate = date(2009, month, day)
weekday = givenDate.strftime("%A")
print(weekday)
