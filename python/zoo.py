from collections import Counter

listNumber = 0
while True:
    numberOfAnimals = int(input())
    if numberOfAnimals == 0:
        break

    animals = Counter()
    for _ in range(numberOfAnimals):
        *type, animal = input().split()
        animal = animal.lower()
        animals[animal] += 1

    listNumber += 1
    print("List {}:".format(listNumber))

    sortedAnimals = sorted(animals.items())
    for animal, occurrences in sortedAnimals:
        print(animal, "|", occurrences)
