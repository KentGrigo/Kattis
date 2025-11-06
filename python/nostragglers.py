numberOfStragglers = 0
numberOfEntries = int(input())
for entryNumber in range(numberOfEntries):
    entryType, direction, count = input().split()
    polarity = 1 if direction == 'IN' else -1
    count = polarity * int(count)
    numberOfStragglers += count

if numberOfStragglers == 0:
    print('NO STRAGGLERS')
else:
    print(numberOfStragglers)
