from collections import deque

height, width = list(map(int, input().split()))
grid = []
for _ in range(height):
    line = list(map(int, list(input())))
    grid.append(line)

startPosition = (0, 0)
endPosition = (width - 1, height - 1)
positionToSteps = {}
positionsAndSteps = deque()
positionsAndSteps.append((startPosition, 0))
while positionsAndSteps:
    position, numberOfSteps = positionsAndSteps.popleft()
    x, y = position
    if not (0 <= x < width and 0 <= y < height):
        continue

    previousNumberOfSteps = positionToSteps.get(position, None)
    if previousNumberOfSteps is None or numberOfSteps < previousNumberOfSteps:
        positionToSteps[position] = numberOfSteps
        if position == endPosition:
            continue

        stepSize = grid[y][x]
        positionsAndSteps.append(((x + stepSize, y), numberOfSteps + 1))
        positionsAndSteps.append(((x - stepSize, y), numberOfSteps + 1))
        positionsAndSteps.append(((x, y + stepSize), numberOfSteps + 1))
        positionsAndSteps.append(((x, y - stepSize), numberOfSteps + 1))

result = positionToSteps.get(endPosition, None)
if result is None:
    print(-1)
else:
    print(result)
