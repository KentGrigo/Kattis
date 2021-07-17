while True:
    try:
        values = list(map(lambda value: int(value), input().split()))
    except EOFError:
        break

    total = sum(values)
    for value in values:
        actualTotal = total - value
        if value == actualTotal:
            print(value)
            break
