numberOfTests = int(input())
for testNumber in range(1, numberOfTests + 1):
    numberOfRows, numberOfColumns = list(map(int, input().split()))
    rows = []
    for _ in range(numberOfRows):
        row = input()[::-1]
        rows.append(row)

    rows = rows[::-1]
    print("Test {}".format(testNumber))
    for row in rows:
        print("".join(row))
