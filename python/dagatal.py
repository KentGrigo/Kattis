import calendar

month = int(input())
year = 2019
(_, numberOfDaysInMonth) = calendar.monthrange(year, month)
print(numberOfDaysInMonth)
