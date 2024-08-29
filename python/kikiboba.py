word = input()

numberOfBs = 0
numberOfKs = 0
for letter in word:
    if letter == 'b':
        numberOfBs += 1
    elif letter == 'k':
        numberOfKs += 1

if numberOfBs == 0 and numberOfKs == 0:
    print("none")
elif numberOfBs < numberOfKs:
    print("kiki")
elif numberOfKs < numberOfBs:
    print("boba")
else:
    print("boki")
