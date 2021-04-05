def test(bricks, height, width):
    heightLeft = height
    widthLeft = width
    brickIndex = 0
    while 0 < heightLeft:
        while 0 < widthLeft:
            brick = bricks[brickIndex]
            if brick <= widthLeft:
                widthLeft -= brick
                brickIndex += 1
            else:
                return False

        heightLeft -= 1
        widthLeft = width

    return True


height, width, numberOfBricks = list(map(int, input().split()))
bricks = list(map(int, input().split()))
isPossible = test(bricks, height, width)
if isPossible:
    print("YES")
else:
    print("NO")
