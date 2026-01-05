midtermGrade1, midtermGrade2, finalExamGrade = list(map(int, input().split()))
weightedScore = 0.25 * midtermGrade1 + 0.25 * midtermGrade2 + 0.5 * finalExamGrade
if weightedScore < 60:
    finalGrade = 'F'
elif weightedScore < 70:
    finalGrade = 'D'
elif weightedScore < 80:
    finalGrade = 'C'
elif weightedScore < 90:
    finalGrade = 'B'
else:
    finalGrade = 'A'

print(finalGrade)
