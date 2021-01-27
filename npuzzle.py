solution = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', '.']
sizeOfPuzzle = 4
allSquares = []
for _ in range(sizeOfPuzzle):
    squares = list(input())
    allSquares.extend(squares)

scatter = 0
for correctPosition, letter in enumerate(solution):
    if letter == '.':
        continue

    correctRow = correctPosition // sizeOfPuzzle
    correctColumn = correctPosition % sizeOfPuzzle

    position = allSquares.index(letter)
    row = position // sizeOfPuzzle
    column = position % sizeOfPuzzle

    difference = abs(correctRow - row) + abs(correctColumn - column)
    scatter += difference

print(scatter)
