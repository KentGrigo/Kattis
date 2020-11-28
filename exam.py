friendsNumberOfCorrectAnswers = int(input())
myAnswers = input()
friendsAnswers = input()

different = 0
same = 0
for myAnswer, friendsAnswer in zip(myAnswers, friendsAnswers):
    if myAnswer == friendsAnswer:
        same += 1
    else:
        different += 1

maxPotentialCorrectAnswers = min(same, friendsNumberOfCorrectAnswers) + min(different, same + different - friendsNumberOfCorrectAnswers)
print(maxPotentialCorrectAnswers)
