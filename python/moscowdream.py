numberOfEasyTasks, numberOfMediumTasks, numberOfHardTasks, \
numberOfNeededTasks = list(map(int, input().split()))
numberOfTasks = numberOfEasyTasks + numberOfMediumTasks + numberOfHardTasks
canConstructDataset = numberOfNeededTasks <= numberOfTasks and \
                        1 <= numberOfEasyTasks and \
                        1 <= numberOfMediumTasks and \
                        1 <= numberOfHardTasks and \
                        3 <= numberOfNeededTasks

if canConstructDataset:
    print("YES")
else:
    print("NO")
