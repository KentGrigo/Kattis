numberOfWorkersKnown = int(input())
numberOfHoursKnown = int(input())
holeSizeInMetresKnown = int(input())

numberOfWorkersGiven = int(input())
holeSizeInMetresGiven = int(input())

workRatio = holeSizeInMetresGiven / holeSizeInMetresKnown
workforceRatio = (numberOfWorkersKnown * numberOfHoursKnown) / numberOfWorkersGiven
numberOfHoursRequired = workRatio * workforceRatio
print(numberOfHoursRequired)
