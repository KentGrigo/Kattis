phraseLength = len(input().split())
numberOfPersons = int(input())
persons = []
for _ in range(numberOfPersons):
    person = input()
    persons.append(person)

team1 = []
team2 = []
index = -1
numberOfPersonsLeft = numberOfPersons
isTeam1 = True
while persons:
    index = (index + phraseLength) % numberOfPersonsLeft
    person = persons.pop(index)
    numberOfPersonsLeft -= 1
    index -= 1
    if isTeam1:
        team1.append(person)
    else:
        team2.append(person)

    isTeam1 = not isTeam1

print(len(team1))
for person in team1:
    print(person)

print(len(team2))
for person in team2:
    print(person)
