class Vertex:
    def __init__(self, number):
        self.number = number
        self.connections = []

    def addConnection(self, other):
        self.connections.append(other)

def interconnection(entryEndpoint, visited):
    needsVisit = []
    needsVisit.append(entryEndpoint)
    for endpoint in needsVisit:
        if endpoint in visited:
            continue

        visited.append(endpoint)
        for connection in endpoint.connections:
            needsVisit.append(endpoints[connection])


numberOfCities = int(input())
for _ in range(numberOfCities):
    numberOfEndpoints = int(input())
    numberOfConnections = int(input())

    endpoints = []
    for endpointNumber in range(numberOfEndpoints):
        endpoint = Vertex(endpointNumber)
        endpoints.append(endpoint)

    for _ in range(numberOfConnections):
        connection1, connection2 = list(map(int, input().split()))
        endpoints[connection1].addConnection(connection2)
        endpoints[connection2].addConnection(connection1)

    visited = []
    numberOfInterconnections = 0
    for entryEndpoint in endpoints:
        if entryEndpoint in visited:
            continue

        numberOfInterconnections += 1
        interconnection(entryEndpoint, visited)

    numberOfMissingRoads = numberOfInterconnections - 1
    print(numberOfMissingRoads)
