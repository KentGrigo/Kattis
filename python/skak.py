(rookX, rookY) = list(map(int, input().split()))
(pawnX, pawnY) = list(map(int, input().split()))

numberOfMovesLeft = 0
if pawnX != rookX:
    numberOfMovesLeft += 1

if pawnY != rookY:
    numberOfMovesLeft += 1

print(numberOfMovesLeft)
