from itertools import permutations
from datetime import date

birthdayOfBash = date(2000, 1, 1)

def test(numbers):
    earliestDate = None
    numberOfPossibleDates = 0
    for permutation in set(permutations(numbers)):
        day = int("".join(permutation[0:2]))
        month = int("".join(permutation[2:4]))
        year = int("".join(permutation[4:]))
        try:
            possibleDate = date(year, month, day)
        except ValueError:
            continue

        if birthdayOfBash <= possibleDate:
            numberOfPossibleDates += 1
            if earliestDate == None or possibleDate < earliestDate:
                earliestDate = possibleDate

    if numberOfPossibleDates == 0:
        print("0")
    else:
        print("{} {:02d} {:02d} {}".format(numberOfPossibleDates, earliestDate.day, earliestDate.month, earliestDate.year))


numberOfTests = int(input())
for _ in range(numberOfTests):
    numbers = filter(lambda symbol: symbol != " ", list(input()))
    test(numbers)
