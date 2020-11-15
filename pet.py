numberOfContestants = 5

bestScore = 0
bestContestant = 1
for contestantNumber in range(1, numberOfContestants + 1):
    pointsOfContestant = sum(map(lambda point: int(point), input().split()))
    if bestScore < pointsOfContestant:
        bestScore = pointsOfContestant
        bestContestant = contestantNumber

print("{} {}".format(bestContestant, bestScore))
