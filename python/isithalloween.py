data = input().split()
month = data[0]
day = int(data[1])

isHalloween = month == "OCT" and day == 31
isChristmas = month == "DEC" and day == 25

if isHalloween or isChristmas:
    print("yup")
else:
    print("nope")
