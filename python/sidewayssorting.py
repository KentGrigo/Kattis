def test(numberOfRows, numberOfColumns):
    rows = []
    for _ in range(numberOfRows):
        row = list(input())
        rows.append(row)

    transposed = [*zip(*rows)]
    transposed.sort(key = lambda entry: list(map(str.casefold, entry)))
    sortedRows = [*zip(*transposed)]
    for sortedRow in sortedRows:
        print("".join(sortedRow))


firstRound = True
while True:
    size = input().split()
    numberOfRows = int(size[0])
    numberOfColumns = int(size[1])
    if numberOfRows == 0 and numberOfColumns == 0:
        break

    if not firstRound:
        print("")
    firstRound = False
    
    test(numberOfRows, numberOfColumns)
