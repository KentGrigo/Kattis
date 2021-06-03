numberOfNames = int(input())
names = []
for _ in range(numberOfNames):
    name = input()
    if len(name) < 5:
        continue

    setOfLetters = set(name)
    if len(setOfLetters) < len(name):
        continue

    names.append(name)

names.sort(key = lambda name: (-len(name), name), reverse = True)
if names:
    print(names[0])
else:
    print("neibb!")
