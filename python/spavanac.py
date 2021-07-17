data = input().split()
hours = int(data[0])
minutes = int(data[1])

if minutes < 45:
    adjustedMinutes = minutes + 15
    if hours == 0:
        adjustedHours = 23
    else:
        adjustedHours = hours - 1
else:
    adjustedMinutes = minutes - 45
    adjustedHours = hours

print("{} {}".format(adjustedHours, adjustedMinutes))