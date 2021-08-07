playerToScore = {}
playerToScore["A"] = 0
playerToScore["B"] = 0

game = input()
for index in range(0, len(game), 2):
    player, points = game[index:index+2]
    playerToScore[player] += int(points)

# There are no ties
isWinnerA = playerToScore["B"] < playerToScore["A"]
if isWinnerA:
    print("A")
else:
    print("B")
