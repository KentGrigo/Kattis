from datetime import datetime, timedelta

format = "%H:%M:%S"
zero = datetime.strptime("00:00:00", format)
midnight = datetime.strptime("00:00:00", format) + timedelta(days = 1)
fromTime = datetime.strptime(input(), format)
toTime = datetime.strptime(input(), format)

if fromTime == toTime:
    print("24:00:00")
elif fromTime < toTime:
    difference = zero + (toTime - fromTime)
    print(difference.time())
else:
    difference = midnight - (fromTime - toTime)
    print(difference.time())
