roomWidth, numberOfPartitions = list(map(int, input().split()))
partitions = list(map(int, input().split()))
partitions.append(0)
partitions.append(roomWidth)

spaces = set()
for partition1 in partitions:
    for partition2 in partitions:
        size = abs(partition1 - partition2)
        if size != 0:
            spaces.add(size)

sortedSpaces = sorted(spaces)
print(" ".join(map(str, sortedSpaces)))
