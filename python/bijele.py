actualPieces = map(lambda piece: int(piece), input().split())
expectedPieces = [1, 1, 2, 2, 2, 8]

difference = [str(expectedPiece - actualPiece) for (expectedPiece, actualPiece) in zip(expectedPieces, actualPieces)]
output = " ".join(difference)
print(output)
