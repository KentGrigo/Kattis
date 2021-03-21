import random

print("1")
while True:
    response = int(input())
    if response == 99:
        break

    remainder = response % 3
    if remainder == 0:
        increment = random.randint(1, 2)
    else:
        increment = 3 - remainder

    answer = response + increment
    print(answer)
    if answer == 99:
        break
