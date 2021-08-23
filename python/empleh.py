def insertPiece(rows, piece, isWhite):
    if len(piece) == 2:
        type = "P"
    elif len(piece) == 3:
        type = piece[0]
    else:
        return

    if not isWhite:
        type = type.lower()

    row = 9 - int(piece[-1])
    rowIndex = 2 * (row - 1) + 1
    column = ord(piece[-2]) - 96
    columnIndex = 4 * (column - 1) + 2

    rows[rowIndex][columnIndex] = type


whiteText = "White: "
blackText = "Black: "
whitePieces = input()[len(whiteText):].split(",")
blackPieces = input()[len(blackText):].split(",")

rows = """\
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+""".splitlines()
rows = list(map(list, rows))

for piece in whitePieces:
    insertPiece(rows, piece, True)

for piece in blackPieces:
    insertPiece(rows, piece, False)

for row in rows:
    print("".join(row))
