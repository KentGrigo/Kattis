data = input().split()
leftTines = int(data[0])
rightTines = int(data[1])

if leftTines == 0 and rightTines == 0:
    print("Not a moose")
elif leftTines == rightTines:
    totalTines = leftTines + rightTines
    print("Even {}".format(totalTines))
else:
    estimatedTines = max(leftTines, rightTines) * 2
    print("Odd {}".format(estimatedTines))
