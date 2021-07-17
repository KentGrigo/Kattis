while True:
    try:
        n = int(input().split("/")[1])
    except EOFError:
        break

    numberOfDivisions = 0
    for y in range(n + 1, 2 * n + 1):
        x = n * y / (y - n)
        if x < y:
            break

        if x.is_integer():
            numberOfDivisions += 1

    print(numberOfDivisions)
