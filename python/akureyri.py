totalNumberOfContestants = int(input())
locationToNumberOfContestants = {}
for _ in range(totalNumberOfContestants):
    input() # not used
    location = input()
    if location not in locationToNumberOfContestants:
        locationToNumberOfContestants[location] = 0

    locationToNumberOfContestants[location] += 1

for location, totalNumberOfContestants in locationToNumberOfContestants.items():
    print(location, totalNumberOfContestants)
