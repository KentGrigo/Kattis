def computeIsStrongVertex(graph, vertex):
    connectedVertices1 = graph[vertex]
    for connectedVertex in connectedVertices1:
        connectedVertices2 = graph[connectedVertex]
        overlap = connectedVertices1.intersection(connectedVertices2)
        if overlap:
            return True

    return False


while True:
    numberOfVertices = int(input())
    if numberOfVertices == -1:
        break

    rows = []
    for _ in range(numberOfVertices):
        row = list(map(int, input().split()))
        rows.append(row)

    graph = {}
    for vertex in range(numberOfVertices):
        graph[vertex] = set()

    for rowIndex, row in enumerate(rows):
        for columnIndex, cell in enumerate(row):
            if rowIndex == columnIndex:
                continue

            isConnected = cell == 1
            if isConnected:
                connectedVertices = graph[rowIndex]
                connectedVertices.add(columnIndex)

    weakVerticies = []
    for vertex in range(numberOfVertices):
        isStrongVertex = computeIsStrongVertex(graph, vertex)
        if not isStrongVertex:
            weakVerticies.append(vertex)

    print(" ".join(map(str, weakVerticies)))
