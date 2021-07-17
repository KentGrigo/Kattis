def test(direction, differenceInMinutes, currentHours, currentMinutes):
    if direction == "F":
        polarity = 1
    else:
        polarity = -1

    newHours = currentHours
    newMinutes = currentMinutes + polarity * differenceInMinutes
    while not (0 <= newMinutes < 60):
        newHours += polarity
        newMinutes += -1 * polarity * 60

    newHours %= 24
    print("{} {}".format(newHours, newMinutes))


numberOfTest = int(input())
for _ in range(numberOfTest):
    data = input().split()
    direction = data[0]
    differenceInMinutes = int(data[1])
    currentHours = int(data[2])
    currentMinutes = int(data[3])
    test(direction, differenceInMinutes, currentHours, currentMinutes)
