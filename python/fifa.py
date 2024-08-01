numberOfImprovements = int(input())
numberOfImprovementsPerYear = int(input())
yearFrozen = 2022
numberOfYearsFrozen = int(numberOfImprovements / numberOfImprovementsPerYear)
currentYear = yearFrozen + numberOfYearsFrozen
print(currentYear)
