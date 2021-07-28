from statistics import mean

def computeEffectiveScore(score, exponent):
    return 1/5 * score * (4/5) ** exponent


numberOfStudents = int(input())
accumulatedScores = [0]
for studentNumber in range(numberOfStudents):
    score = int(input())
    totalScore = accumulatedScores[0]
    accumulatedScores[0] += computeEffectiveScore(score, studentNumber)
    for index, _ in enumerate(accumulatedScores[1:], 1):
        exponent = studentNumber - 1
        accumulatedScores[index] += computeEffectiveScore(score, exponent)

    accumulatedScores.append(totalScore)

print(accumulatedScores[0])
print(mean(accumulatedScores[1:]))
