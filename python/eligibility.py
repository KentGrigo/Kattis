from datetime import date

def computeEligibility(dateOfPostSecondaryStudies, dateOfBirth, numberOfCourses):
    if date(2010, 1, 1).__le__(dateOfPostSecondaryStudies):
        return "eligible"
    elif date(1991, 1, 1).__le__(dateOfBirth):
        return "eligible"
    elif 41 <= numberOfCourses:
        return "ineligible"
    else:
        return "coach petitions"

def convertToDate(dateString):
    year, month, day = list(map(int, dateString.split("/")))
    return date(year, month, day)


numberOfCases = int(input())
for _ in range(numberOfCases):
    name, dateOfPostSecondaryStudies, dateOfBirth, numberOfCourses = input().split()
    dateOfPostSecondaryStudies = convertToDate(dateOfPostSecondaryStudies)
    dateOfBirth = convertToDate(dateOfBirth)
    numberOfCourses = int(numberOfCourses)

    eligibility = computeEligibility(dateOfPostSecondaryStudies, dateOfBirth, numberOfCourses)
    print("{} {}".format(name, eligibility))
