numberOfRooms, numberOfBookedRooms = list(map(int, input().split()))
bookedRooms = set()
for bookedRoom in range(numberOfRooms):
    bookedRooms.add(str(bookedRoom + 1))

for _ in range(numberOfBookedRooms):
    bookedRoom = input()
    bookedRooms.remove(bookedRoom)

if bookedRooms:
    print(bookedRooms.pop())
else:
    print("too late")
