def press(numberOfPresses, numberOfAs, numberOfBs):
    if numberOfPresses == 0:
        return (numberOfAs, numberOfBs)
    else:
        return press(numberOfPresses - 1, numberOfBs, numberOfAs + numberOfBs)

numberOfPresses = int(input())
numberOfAs, numberOfBs = press(numberOfPresses, 1, 0)
print(numberOfAs, numberOfBs)
