left, middle, right = list(map(int, input().split()))
maxNumberOfMoves = max(middle - left, right - middle) - 1
print(maxNumberOfMoves)
