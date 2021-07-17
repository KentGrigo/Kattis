numberOfTiles = int(input())
tiles = list(map(int, input().split()))
tiles.sort()
score = 0
for tile1, tile2 in zip(tiles[:-1], tiles[1:]):
    score += (tile1 - tile2) ** 2

print(score)
