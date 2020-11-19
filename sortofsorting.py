import functools

def compare(name1, name2):
    if name1[0] < name2[0]:
        return -1
    elif name2[0] < name1[0]:
        return 1
    elif name1[1] < name2[1]:
        return -1
    elif name2[1] < name1[1]:
        return 1
    else:
        return 0

firstIteration = True
while True:
    numberOfNames = int(input())
    if numberOfNames == 0:
        break

    if not firstIteration:
        print("")
    firstIteration = False

    names = []
    for _ in range(numberOfNames):
        name = input()
        names.append(name)
    
    names.sort(key=functools.cmp_to_key(compare))
    for name in names:
        print(name)
