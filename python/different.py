while True:
    try:
        numbers = input().split()
    except EOFError:
        break

    number1 = int(numbers[0])
    number2 = int(numbers[1])
    print(abs(number1 - number2))
