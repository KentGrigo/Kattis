firstNames = {}
fullNames = []
while True:
    try:
        firstName, lastName = input().split()
    except EOFError:
        break

    fullName = (lastName, firstName)
    fullNames.append(fullName)
    firstNames[firstName] = 1 + firstNames.get(firstName, 0)

fullNames.sort()
for fullName in fullNames:
    lastName, firstName = fullName
    occurrencesOfFirstName = firstNames[firstName]
    if 1 < occurrencesOfFirstName:
        print(firstName, lastName)
    else:
        print(firstName)
