minuteRate = 0.10 # $/minute
dayNumber = 1
while True:
    # Check for "OPEN"
    try:
        _ = input() 
    except EOFError:
        break

    # Check for entries until "CLOSE"
    entries = {}
    totalEntries = {}
    while True:
        entry = input().split()
        command = entry[0]
        if command == "CLOSE":
            break

        name = entry[1]
        time = int(entry[2])
        if command == "ENTER":
            entries[name] = time

        if command == "EXIT":
            timeDifference = time - entries[name]
            totalEntries[name] = timeDifference + totalEntries.get(name, 0)

    if 1 < dayNumber:
        print("")

    print("Day {}".format(dayNumber))
    for name, timeSpent in sorted(totalEntries.items()):
        bill = timeSpent * minuteRate
        print("{} ${:.2f}".format(name, bill))

    dayNumber += 1
