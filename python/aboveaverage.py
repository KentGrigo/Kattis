def test(numberOfPeople, grades):
    sum = 0
    for grade in grades:
        sum += grade

    average = sum / numberOfPeople
    numberOfPeopleAboveAverage = 0
    for grade in grades:
        if average < grade:
            numberOfPeopleAboveAverage += 1

    percentageOfPeopleAboveAverage = numberOfPeopleAboveAverage / numberOfPeople * 100
    print("{:.3f}%".format(percentageOfPeopleAboveAverage))


numberOfTests = int(input())
for _ in range(numberOfTests):
    numberOfPeople, *grades = list(map(int, input().split()))
    test(numberOfPeople, grades)
