width = int(input())
numberOfPieces = int(input())

totalArea = 0
for _ in range(numberOfPieces):
    piece = input().split()
    pieceWidth = int(piece[0])
    pieceLength = int(piece[1])

    totalArea += pieceWidth * pieceLength

length = int(totalArea / width)
print(length)