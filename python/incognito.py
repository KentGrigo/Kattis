numberOfTests = int(input())
for _ in range(numberOfTests):
    categoryToName = {}
    numberOfAttributes = int(input())
    for _ in range(numberOfAttributes):
        name, category = input().split()
        names = categoryToName.get(category, [])
        names.append(name)
        categoryToName[category] = names

    numberOfDisguises = 1
    for names in categoryToName.values():
        numberOfDisguises *= len(names) + 1

    numberOfDisguises -= 1
    print(numberOfDisguises)
