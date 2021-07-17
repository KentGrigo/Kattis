numberOfPapers = int(input())
citations = []
for _ in range(numberOfPapers):
    numberOfCitations = int(input())
    citations.append(numberOfCitations)

citations.sort(reverse = True)

hIndex = 0
for numberOfPapersWithCitations, numberOfCitations in zip(range(1, numberOfPapers + 1), citations):
    if numberOfPapersWithCitations <= numberOfCitations:
        hIndex = numberOfPapersWithCitations

print(hIndex)
