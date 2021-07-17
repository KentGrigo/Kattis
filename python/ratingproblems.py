minRating = -3
maxRating = 3
numberOfJudges, numberOfJudgedJudges = list(map(int, input().split()))

totalRating = 0
for _ in range(numberOfJudgedJudges):
    rating = int(input())
    totalRating += rating

numberOfUnjudgedJudges = numberOfJudges - numberOfJudgedJudges
minTotalRatings = (totalRating + minRating * numberOfUnjudgedJudges) / numberOfJudges
maxTotalRatings = (totalRating + maxRating * numberOfUnjudgedJudges) / numberOfJudges
print(minTotalRatings, maxTotalRatings)
