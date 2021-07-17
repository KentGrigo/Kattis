from collections import Counter

groupSize = int(input())
outcomes = list(map(int, input().split()))
counter = Counter(outcomes)
highestUniqueOutcome = None
for outcome, occurrences in counter.most_common()[::-1]:
    if occurrences != 1:
        break

    if highestUniqueOutcome == None:
        highestUniqueOutcome = outcome
    else:
        highestUniqueOutcome = max(highestUniqueOutcome, outcome)

if highestUniqueOutcome == None:
    print("none")
else:
    indexOfParticipant = outcomes.index(highestUniqueOutcome) + 1
    print(indexOfParticipant)
