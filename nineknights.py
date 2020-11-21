boardSize = 5
board = []
for _ in range(boardSize):
    boardRow = input()
    board.append(boardRow)

numberOfKnights = 0
for row in board:
    for cell in row:
        if cell == "k":
            numberOfKnights += 1

def lookup(board, rowIndex, cellIndex):
    if 0 <= rowIndex and rowIndex < boardSize and 0 <= cellIndex and cellIndex < boardSize:
        return board[rowIndex][cellIndex]
    else:
        return "."

movements = [(-2, -1), (-2, 1), (2, -1), (2, 1),
             (-1, -2), (-1, 2), (1, -2), (1, 2)]
def isValidSolution():
    for rowIndex, row in enumerate(board):
        for cellIndex, cell in enumerate(row):
            if cell == ".":
                continue

            for movement in movements:
                newRowIndex = rowIndex + movement[0]
                newCellIndex = cellIndex + movement[1]
                newCell = lookup(board, newRowIndex, newCellIndex)
                if newCell == "k":
                    return False

    return True

if numberOfKnights == 9 and isValidSolution():
    print("valid")
else:
    print("invalid")
