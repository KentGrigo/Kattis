class Piece:
    def __init__(self, type, color, row, column):
        self.type = type.upper()
        self.color = color
        self.row = row
        self.column = column

    def __lt__(self, other):
        if self.color != other.color:
            raise Exception("Cannot compare")

        if self.typeValue() != other.typeValue():
            return self.typeValue() < other.typeValue()

        if self.color == "White" and self.row != other.row:
            return self.row < other.row

        if self.color == "Black" and self.row != other.row:
            return other.row < self.row

        return self.column < other.column

    def typeValue(self):
        types = ["K", "Q", "R", "B", "N", "P"]
        return types.index(self.type)

    def __str__(self):
        column = chr(self.column + 96)
        if self.type == "P":
            output = "{}{}".format(column, self.row)
        else:
            output = "{}{}{}".format(self.type, column, self.row)
        return output


numberOfRows = 8
whitePieces = []
blackPieces = []
rows = []

input()
for rowNumber in range(numberOfRows, 0, -1):
    row = input()
    input()
    rows.append(row)

for rowNumber, row in enumerate(rows):
    rowNumber = numberOfRows - rowNumber
    for columnNumber, field in enumerate(row[2::4], 1):
        if field != "." and field != ":":
            if field.islower():
                color = "Black"
                piece = Piece(field, color, rowNumber, columnNumber)
                blackPieces.append(piece)
            else:
                color = "White"
                piece = Piece(field, color, rowNumber, columnNumber)
                whitePieces.append(piece)

whitePieces.sort()
blackPieces.sort()
print("White: " + ",".join(map(str, whitePieces)))
print("Black: " + ",".join(map(str, blackPieces)))
