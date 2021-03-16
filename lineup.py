numberOfPeople = int(input())

previousPerson = None
sortingDirection = None
for _ in range(numberOfPeople):
    currentPerson = input()
    if previousPerson is not None:
        if sortingDirection is None:
            if previousPerson < currentPerson:
                sortingDirection = "INCREASING"
            elif currentPerson < previousPerson:
                sortingDirection = "DECREASING"
        if sortingDirection == "DECREASING" and previousPerson < currentPerson or \
            sortingDirection == "INCREASING" and currentPerson < previousPerson:
                sortingDirection = "NEITHER"

    previousPerson = currentPerson

print(sortingDirection)
