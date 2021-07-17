from collections import Counter

categoryToAssociatedWords = {}
numberOfCategories = int(input())
for _ in range(numberOfCategories):
    category, numberOfAssociatedWords, *associatedWords = input().split()
    categoryToAssociatedWords[category] = associatedWords

words = []
while True:
    try:
        line = input().split()
        words.extend(line)
    except EOFError:
        break

maxCategoryScore = 0
matchingCategories = []
occurrencesOfWords = Counter(words)
for category, associatedWords in categoryToAssociatedWords.items():
    categoryScore = 0
    for associatedWord in associatedWords:
        categoryScore += occurrencesOfWords[associatedWord]

    if maxCategoryScore == categoryScore:
        matchingCategories.append(category)
    elif maxCategoryScore < categoryScore:
        maxCategoryScore = categoryScore
        matchingCategories = [category]

matchingCategories.sort()
for matchingCategory in matchingCategories:
    print(matchingCategory)
