def minimum(value1, value2):
    if value1 is None:
        return value2
    elif value2 is None:
        return value1
    else:
        return min(value1, value2)

def flipColor(color):
    if color == white:
        return black
    else:
        return white

def isWithinBounds(x, y):
    return 0 <= x < width and 0 <= y < height

def flipCell(grid, x, y):
    if isWithinBounds(x, y):
        index = y * width + x
        grid[index] = flipColor(grid[index])

def flip(grid, index):
    flippedGrid = grid.copy()
    x = index % width
    y = index // width
    flipCell(flippedGrid, x, y)
    flipCell(flippedGrid, x + 1, y)
    flipCell(flippedGrid, x - 1, y)
    flipCell(flippedGrid, x, y + 1)
    flipCell(flippedGrid, x, y - 1)
    return flippedGrid

def isAllWhite(grid):
    for cell in grid:
        if cell == black:
            return False

    return True

def convert(grid):
    def helper(grid, numberOfFlips, index):
        if isAllWhite(grid):
            return numberOfFlips

        if height * width <= index:
            return None

        result1 = helper(grid, numberOfFlips, index + 1)
        result2 = helper(flip(grid, index), numberOfFlips + 1, index + 1)
        return minimum(result1, result2)

    return helper(grid, 0, 0)


black = "*"
white = "."
height = 3
width = 3
numberOfProblems = int(input())
for _ in range(numberOfProblems):
    grid = []
    for _ in range(height):
        row = list(input())
        grid.extend(row)

    minimumNumberOfFlips = convert(grid)
    print(minimumNumberOfFlips)
