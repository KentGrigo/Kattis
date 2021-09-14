numberOfMeasurements = int(input())
totalSecondsGiven = 0
totalSecondsTaken = 0
for _ in range(numberOfMeasurements):
    minutesGiven, secondsTaken = list(map(int, input().split()))
    secondsGiven = minutesGiven * 60
    totalSecondsGiven += secondsGiven
    totalSecondsTaken += secondsTaken

if totalSecondsTaken <= totalSecondsGiven:
    print("measurement error")
else:
    print(totalSecondsTaken / totalSecondsGiven)
