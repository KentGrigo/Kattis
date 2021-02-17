min = 1
max = 1001
while True:
    guess = min + (max - min) // 2
    print(guess)
    response = input()
    if response == "correct":
        break

    if response == "higher":
        min = guess
    else:
        max = guess
