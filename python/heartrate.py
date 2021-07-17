numberOfCases = int(input())
for _ in range(numberOfCases):
    data = input().split()
    numberOfBeats = int(data[0])
    numberOfSeconds = float(data[1])
    bpm = 60 * numberOfBeats / numberOfSeconds
    difference = 60 / numberOfSeconds
    lowerAbmp = bpm - difference
    higherAbmp = bpm + difference
    print("{} {} {}".format(
            round(lowerAbmp, 4), 
            round(bpm, 4),
            round(higherAbmp, 4)
    ))
