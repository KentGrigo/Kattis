numberOfCharacters = int(input())
numberOfSubsets = 2 ** numberOfCharacters
numberOfRelationships = numberOfSubsets - numberOfCharacters - 1
print(numberOfRelationships)
