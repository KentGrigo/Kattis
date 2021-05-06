daysOfWeek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
monthToOffset = {
    "JAN": 0,
    "FEB": 3,
    "MAR": 3,
    "APR": 6,
    "MAY": 1,
    "JUN": 4,
    "JUL": 6,
    "AUG": 2,
    "SEP": 5,
    "OCT": 0,
    "NOV": 3,
    "DEC": 5,
}
monthToLeapYearOffset = {
    "JAN": 0,
    "FEB": 3,
    "MAR": 4,
    "APR": 0,
    "MAY": 2,
    "JUN": 3,
    "JUL": 0,
    "AUG": 3,
    "SEP": 6,
    "OCT": 1,
    "NOV": 4,
    "DEC": 6,
}

dayOfInterest = input().split()
day = int(dayOfInterest[0])
month = dayOfInterest[1]
jan1stDay = daysOfWeek.index(input())

weekdayOffset = (jan1stDay + monthToOffset[month] + (day - 1)) % (len(daysOfWeek))
weekdayLeapYearOffset = (jan1stDay + monthToLeapYearOffset[month] + (day - 1)) % (len(daysOfWeek))
weekday = daysOfWeek[weekdayOffset]
weekdayLeapYear = daysOfWeek[weekdayLeapYearOffset]

if weekday == "FRI" and weekdayLeapYear == "FRI":
    print("TGIF")
elif weekday == "FRI" or weekdayLeapYear == "FRI":
    print("not sure")
else:
    print(":(")
