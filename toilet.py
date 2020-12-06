def changesForAlwaysUp(initialPosition, preference):
    changes = 0
    previousPosition = initialPosition
    for preference in preferences:
        if preference != previousPosition:
            changes += 1
        if preference == "D":
            changes += 1
        previousPosition = "U"
    return changes

def changesForAlwaysDown(initialPosition, preference):
    changes = 0
    previousPosition = initialPosition
    for preference in preferences:
        if preference != previousPosition:
            changes += 1
        if preference == "U":
            changes += 1
        previousPosition = "D"
    return changes

def changesForAsIs(initialPosition, preference):
    changes = 0
    previousPosition = initialPosition
    for preference in preferences:
        if preference != previousPosition:
            changes += 1
        previousPosition = preference
    return changes


sequence = input()
initialPosition = sequence[0]
preferences = sequence[1:]

changesForAlwaysSeatUp = changesForAlwaysUp(initialPosition, preferences)
changesForAlwaysSeatDown = changesForAlwaysDown(initialPosition, preferences)
changesForSeatAsIs = changesForAsIs(initialPosition, preferences)

print(changesForAlwaysSeatUp)
print(changesForAlwaysSeatDown)
print(changesForSeatAsIs)
