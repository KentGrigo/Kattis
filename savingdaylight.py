from datetime import datetime
import sys

while True:
    try:
        line = input()
    except EOFError:
        break
    if line == "":
        break

    timestamp = line.split()
    date = " ".join(timestamp[0:3])
    morning = datetime.strptime(timestamp[-2], "%H:%M")
    evening = datetime.strptime(timestamp[-1], "%H:%M")
    timeSunIsUp = "{}".format(evening - morning).split(":")
    hoursSunIsUp = timeSunIsUp[0]
    minutesSunIsUp = int(timeSunIsUp[1])
    print("{} {} hours {} minutes".format(date, hoursSunIsUp, minutesSunIsUp))
