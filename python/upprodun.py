from math import floor

numberOfRooms = int(input())
numberOfTeams = int(input())

averageTeamsPerRoom = numberOfTeams / numberOfRooms
accumulatedTeams = 0
previousLeftover = numberOfTeams
while 0 < previousLeftover:
    accumulatedTeams += averageTeamsPerRoom
    currentLeftover = floor(numberOfTeams - accumulatedTeams)
    numberOfTeamsInRoom = previousLeftover - currentLeftover
    print("*" * numberOfTeamsInRoom)
    previousLeftover = currentLeftover
