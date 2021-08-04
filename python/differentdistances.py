while True:
    data = input()
    if data == "0":
        break

    x1, y1, x2, y2, p = list(map(float, data.split()))
    diffX = abs(x2 - x1)
    diffY = abs(y2 - y1)
    distance = (diffX ** p + diffY ** p) ** (1 / p)
    print(distance)
