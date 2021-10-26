def getGrade(score):
    for index, limit in enumerate(limits):
        if limit <= score:
            return grades[index]

    return grades[-1]


grades = ["A", "B", "C", "D", "E", "F"]
limits = list(map(int, input().split()))
score = int(input())
grade = getGrade(score)
print(grade)
