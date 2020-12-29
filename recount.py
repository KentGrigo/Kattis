votes = {}
while True:
    vote = input()
    if vote == "***":
        break

    votes[vote] = votes.get(vote, 0) + 1

winner = None
winningCount = 0
multipleWinners = False
for vote, count in votes.items():
    if winningCount < count:
        winner = vote
        winningCount = count
        multipleWinners = False
    elif winningCount == count:
        multipleWinners = True

if multipleWinners:
    print("Runoff!")
else:
    print(winner)
