x = int(input())
y = int(input())

isRightYAxis = 0 < x
isAboveXAxis = 0 < y
if isRightYAxis and isAboveXAxis:
    print("1")
elif not isRightYAxis and isAboveXAxis:
    print("2")
elif not isRightYAxis and not isAboveXAxis:
    print("3")
else:
    print("4")
