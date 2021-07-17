data = input().split()
numberOfRows = int(data[0])
numberOfColumns = int(data[1])
numberOfClasses = int(data[2])

rows = []
for _ in range(numberOfRows):
    row = list(input())
    rows.append(row)

classesDependentOnOthers = {}
for columnIndex in range(numberOfColumns):
    minimumClass = rows[0][columnIndex]
    for rowIndex in range(numberOfRows):
        currentClass = rows[rowIndex][columnIndex]
        minimumClass = min(minimumClass, currentClass)

    for rowIndex in range(numberOfRows):
        currentClass = rows[rowIndex][columnIndex]
        if minimumClass < currentClass:
            if currentClass in classesDependentOnOthers:
                previousMinimumClass = classesDependentOnOthers[currentClass]
                if minimumClass < previousMinimumClass:
                    classesDependentOnOthers[currentClass] = minimumClass    
            else:
                classesDependentOnOthers[currentClass] = minimumClass

differentColors = numberOfClasses - len(classesDependentOnOthers)
print(differentColors)
