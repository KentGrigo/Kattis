size = int(input())
columnBalances = [0] * size
columnLastSeen = ['-'] * size
columnLastSeenCount = [0] * size
black = 'B'
white = 'W'

isCorrect = True
for _ in range(size):
    row = input()
    rowBalance = 0
    for index, cell in enumerate(row):
        if cell == black:
            rowBalance += 1
            columnBalances[index] += 1
        else:
            rowBalance -= 1
            columnBalances[index] -= 1

        if columnLastSeen[index] != cell:
            columnLastSeen[index] = cell
            columnLastSeenCount[index] = 0

        columnLastSeenCount[index] += 1
        if 3 <= columnLastSeenCount[index]:
            isCorrect = False
        
    if rowBalance != 0:
        isCorrect = False

for columnBalance in columnBalances:
    if columnBalance != 0:
        isCorrect = False

if isCorrect:
    print(1)
else:
    print(0)
