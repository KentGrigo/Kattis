numberOfBlocks = int(input())
height = 0
while True:
    numberOfBlocksForLayer = (height * 2 + 1) ** 2
    numberOfBlocks -= numberOfBlocksForLayer
    if numberOfBlocks < 0:
        break

    height += 1

print(height)
