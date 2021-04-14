numberOfTests = int(input())
for _ in range(numberOfTests):
    sumOfScores, differenceOfScores = list(map(int, input().split()))
    halfScore = sumOfScores / 2
    halfDifference = differenceOfScores / 2
    score1 = int(halfScore + halfDifference)
    score2 = int(halfScore - halfDifference)
    isScoreNegative = score1 < 0 or score2 < 0
    isScoreMismatching = score1 + score2 != sumOfScores or abs(score1 - score2) != differenceOfScores
    if isScoreNegative or isScoreMismatching:
        print("impossible")
    else:
        print("{} {}".format(score1, score2))
