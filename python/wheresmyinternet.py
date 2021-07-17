def addConnection(connections, house1, house2):
    house1Connections = connections.get(house1, [])
    house1Connections.append(house2)
    connections[house1] = house1Connections


numberOfHouses, numberOfConnections = list(map(int, input().split()))
connections = {}
connections[1] = []
for _ in range(numberOfConnections):
    house1, house2 = list(map(int, input().split()))
    addConnection(connections, house1, house2)
    addConnection(connections, house2, house1)

visitedConnections = set()
unvisitedConnections = set()
newConnections = set()
newConnections.add(1)
while newConnections:
    unvisitedConnections = newConnections
    newConnections = set()
    for connectedHouse in unvisitedConnections:
        houseConnections = connections[connectedHouse]
        for houseConnection in houseConnections:
            if houseConnection not in visitedConnections and houseConnection not in unvisitedConnections:
                newConnections.add(houseConnection)

    visitedConnections.update(unvisitedConnections)

allHouses = set(range(1, numberOfHouses + 1))
housesMissingConnection = allHouses.difference(visitedConnections)
if housesMissingConnection:
    for unconnectedHouse in housesMissingConnection:
        print(unconnectedHouse)
else:
    print("Connected")
