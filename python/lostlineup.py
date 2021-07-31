numberOfFriends = int(input())
offsets = list(map(int, input().split()))

offsetToPosition = {}
for position, offset in enumerate(offsets, 2):
    offsetToPosition[offset] = position

lineup = [1]
for offset in range(numberOfFriends - 1):
    position = offsetToPosition[offset]
    lineup.append(position)

print(" ".join(map(str, lineup)))
