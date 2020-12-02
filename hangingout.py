metadata = input().split()
safetyLimit = int(metadata[0])
numberOfEvents = int(metadata[1])

numberOfPeople = 0
deniedGroups = 0
for _ in range(numberOfEvents):
    event = input().split()
    eventType = event[0]
    groupSize = int(event[1])
    if eventType == "enter":
        newNumberOfPeople = numberOfPeople + groupSize
    else:
        newNumberOfPeople = numberOfPeople - groupSize

    if safetyLimit < newNumberOfPeople:
        deniedGroups += 1
    else:
        numberOfPeople = newNumberOfPeople

print(deniedGroups)
