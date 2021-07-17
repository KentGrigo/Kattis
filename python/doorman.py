margin = int(input())
persons = list(input())

buffer = None
numberOfMen = 0
numberOfWomen = 0
for person in persons:
    difference = numberOfMen - numberOfWomen
    if buffer != None and -margin < difference < margin:
        if buffer == "M":
            numberOfMen += 1
        else:
            numberOfWomen += 1
        buffer = None

    if person == "M":
        if difference < margin:
            numberOfMen += 1
        elif buffer == None:
            buffer = person
        else:
            break
    else:
        if -margin < difference:
            numberOfWomen += 1
        elif buffer == None:
            buffer = person
        else:
            break

print(numberOfMen + numberOfWomen)
