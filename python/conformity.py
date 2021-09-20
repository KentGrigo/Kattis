numberOfFrosh = int(input())
courseCombinations = {}
for _ in range(numberOfFrosh):
    courseCombination = tuple(sorted(input().split()))
    courseCombinations[courseCombination] = 1 + courseCombinations.get(courseCombination, 0)

popularCourseSize = max(courseCombinations.values())
numberOfFroshWithMostPopularCombination = sum(filter(lambda courseSize: courseSize == popularCourseSize, courseCombinations.values()))
print(numberOfFroshWithMostPopularCombination)
