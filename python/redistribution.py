def test(rooms):
    roomNumberToRoom = {}
    for roomNumber, room in enumerate(rooms, 1):
        roomNumberToRoom[roomNumber] = room

    roomNumberAndRooms = list(sorted(roomNumberToRoom.items(), key=lambda item: -item[1]))

    papers = []
    for roomNumber, room in roomNumberAndRooms:
        for _ in range(room):
            papers.append(roomNumber)
    
    students = []
    for roomNumber, room in roomNumberAndRooms[1:]:
        for _ in range(room):
            students.append(roomNumber)

    for roomNumber, room in roomNumberAndRooms[0:1]:
        for _ in range(room):
            students.append(roomNumber)

    for paper, student in zip(papers, students):
        if paper == student:
            return None

    return [roomNumber for roomNumber, _ in roomNumberAndRooms]


numberOfRooms = int(input())
rooms = list(map(int, input().split()))
result = test(rooms)
if result == None:
    print("impossible")
else:
    print(*result)
