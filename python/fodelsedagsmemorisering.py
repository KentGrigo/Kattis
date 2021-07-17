numberOfFriends = int(input())
dateToNameAndScore = {}
for _ in range(numberOfFriends):
    name, score, date = input().split()
    score = int(score)
    if date not in dateToNameAndScore:
        dateToNameAndScore[date] = (name, score)
    else:
        _, savedScore = dateToNameAndScore[date]
        if savedScore < score:
            dateToNameAndScore[date] = (name, score)

savedNames = [name for name, _ in dateToNameAndScore.values()]
savedNames.sort()
print(len(savedNames))
for name in savedNames:
    print(name)
