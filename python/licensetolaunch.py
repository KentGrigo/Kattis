numberOfLaunchDays = int(input())
amountOfSpaceJunk = list(map(lambda spaceJunk: int(spaceJunk), input().split()))

bestDayForLaunch = amountOfSpaceJunk.index(min(amountOfSpaceJunk))
print(bestDayForLaunch)
