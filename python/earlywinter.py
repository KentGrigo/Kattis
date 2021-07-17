data = input().split()
numberOfPreviousWinters = int(data[0])
thisWinter = int(data[1])
previousWinters = list(map(lambda winter: int(winter), input().split()))

numberOfLaterWinters = 0
for previousWinter in previousWinters:
    if previousWinter <= thisWinter:
        break
    else:
        numberOfLaterWinters += 1

if numberOfLaterWinters == numberOfPreviousWinters:
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in {} years!".format(numberOfLaterWinters))
