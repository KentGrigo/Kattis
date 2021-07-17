numberOfGroups = int(input())
for _ in range(numberOfGroups):
    numberOfGnomes, *gnomes = list(map(int, input().split()))
    previousGnome = gnomes[0]
    for index, currentGnome in enumerate(gnomes[1:], 1):
        if previousGnome + 1 != currentGnome:
            print(index + 1)
            break

        previousGnome = currentGnome
