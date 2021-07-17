def test(boardSize):
    if boardSize == 0 or boardSize == 1:
        numberOfBishops = boardSize
    else:
        numberOfBishops = (boardSize - 1) * 2

    print(numberOfBishops)


while True:
    try:
        boardSize = int(input())
    except EOFError:
        break

    test(boardSize)
