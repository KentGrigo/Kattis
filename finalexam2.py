numberOfQuestions = int(input())
previousAnswer = input()
numberOfCorrectAnswers = 0
for _ in range(numberOfQuestions - 1):
    currentAnswer = input()
    if previousAnswer == currentAnswer:
        numberOfCorrectAnswers += 1

    previousAnswer = currentAnswer

print(numberOfCorrectAnswers)
