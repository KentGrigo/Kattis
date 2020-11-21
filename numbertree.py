data = input().split()
treeHeight = int(data[0])
rootNumber = 2 ** (treeHeight + 1) - 1
if len(data) == 1:
    print(rootNumber)
    exit()

directions = data[1]
nodeNumber = rootNumber
layerSize = 1
for direction in directions[::-1]:
    if direction == "R":
        layerSize *= 2
        nodeNumber -= layerSize
    else:
        nodeNumber -= layerSize
        layerSize *= 2

print(nodeNumber)
