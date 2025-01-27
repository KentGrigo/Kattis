numberOfProblems = int(input())
numberOfTeams = int(input())
problemNames = input().split()
totalScores = [0] * len(problemNames)
for _ in range(numberOfTeams):
    scores = list(map(int, input().split()))
    for index, score in enumerate(scores):
        totalScores[index] += score

easiestProblem = problemNames[0]
highestScore = totalScores[0]
for problemName, totalScore in zip(problemNames, totalScores):
    if highestScore < totalScore:
        easiestProblem = problemName
        highestScore = totalScore

print(easiestProblem)
