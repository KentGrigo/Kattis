data = input().split()
numberOfArticles = int(data[0])
impactFactor = int(data[1])

numberOfCitations = numberOfArticles * (impactFactor - 1) + 1
print(numberOfCitations)