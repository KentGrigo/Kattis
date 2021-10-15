while True:
    side1, side2, side3 = sorted(map(int, input().split()))
    if side1 == 0 and side2 == 0 and side3 == 0:
        break

    if side1 ** 2 + side2 ** 2 == side3 ** 2:
        print("right")
    else:
        print("wrong")
