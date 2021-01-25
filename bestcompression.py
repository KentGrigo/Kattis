data = input().split()
numberOfFiles = int(data[0])
maximumNumberOfBits = int(data[1])

needed = 2 ** (maximumNumberOfBits + 1)
if numberOfFiles < needed:
    print("yes")
else:
    print("no")
