while True:
    minValue = 1
    maxValue = 10
    guess = int(input())
    if guess == 0:
        break

    while True:
        response = input()
        if response == "too high":
            maxValue = min(maxValue, guess - 1)

        elif response == "too low":
            minValue = max(minValue, guess + 1)

        else: # "right on"
            isWithinBounds = minValue <= guess <= maxValue
            if isWithinBounds:
                print("Stan may be honest")
            else:
                print("Stan is dishonest")

            break

        guess = int(input())
